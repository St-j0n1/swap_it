from rest_framework import viewsets, views, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404

from .models import (
    Item, Book, Clothes, Game, Technic,
    StereoSystem, PC, Console, Mobile,
    TV, Monitor,
    CPU, GPU, RAM, Storage,
    Xbox, PlayStation, Nintendo
)
from .serializers import (
    ItemSerializer, BookSerializer, ClothesSerializer, GameSerializer, TechnicSerializer,
    StereoSystemSerializer, PCSerializer, ConsoleSerializer, MobileSerializer,
    TVSerializer, MonitorSerializer,
    CPUSerializer, GPUSerializer, RAMSerializer, StorageSerializer,
    XboxSerializer, PlayStationSerializer, NintendoSerializer
)


class ItemTypeChoiceView(views.APIView):
    def get(self, request):
        item_types = [
            {"id": "book", "name": "Book", "description": "Books and publications"},
            {"id": "clothes", "name": "Clothes", "description": "Clothing items"},
            {"id": "game", "name": "Game", "description": "Video games"},
            {"id": "technic", "name": "Technic", "description": "Technical devices and components"}
        ]
        return Response(item_types)


class TechnicCategoryChoiceView(views.APIView):
    """
    View to provide the technic categories for selection
    """

    def get(self, request):
        categories = [
            {"id": "stereo_system", "name": "Stereo System", "description": "Television and monitor devices"},
            {"id": "pc", "name": "PC", "description": "Personal computers and components"},
            {"id": "console", "name": "Console", "description": "Gaming consoles"},
            {"id": "mobile", "name": "Mobile", "description": "Mobile devices"}
        ]
        return Response(categories)


class TechnicSubcategoryChoiceView(views.APIView):
    """
    View to provide subcategories based on the selected technic category
    """

    def get(self, request, category):
        subcategories = {
            "stereo_system": [
                {"id": "tv", "name": "TV", "model": "TV"},
                {"id": "monitor", "name": "Monitor", "model": "Monitor"}
            ],
            "pc": [
                {"id": "cpu", "name": "CPU", "model": "CPU"},
                {"id": "gpu", "name": "GPU", "model": "GPU"},
                {"id": "ram", "name": "RAM", "model": "RAM"},
                {"id": "storage", "name": "Storage", "model": "Storage"}
            ],
            "console": [
                {"id": "xbox", "name": "Xbox", "model": "Xbox"},
                {"id": "playstation", "name": "PlayStation", "model": "PlayStation"},
                {"id": "nintendo", "name": "Nintendo", "model": "Nintendo"}
            ],
            "mobile": []  # Mobile doesn't have subcategories in our model
        }

        if category not in subcategories:
            return Response({"error": "Invalid category"}, status=status.HTTP_400_BAD_REQUEST)

        return Response(subcategories[category])


class ItemCreateView(views.APIView):
    """
    View to create items based on the selected item type
    """

    def get_serializer_class(self, item_type):
        """
        Get the appropriate serializer class based on item type
        """
        serializer_map = {
            "book": BookSerializer,
            "clothes": ClothesSerializer,
            "game": GameSerializer,
            "technic": TechnicSerializer
        }

        return serializer_map.get(item_type)

    def get_model_class(self, item_type):
        """
        Get the appropriate model class based on item type
        """
        model_map = {
            "book": Book,
            "clothes": Clothes,
            "game": Game,
            "technic": Technic
        }

        return model_map.get(item_type)

    def get(self, request, item_type):
        """
        Get the form fields required for creating an item of the selected type
        """
        serializer_class = self.get_serializer_class(item_type)
        if not serializer_class:
            return Response({"error": "Invalid item type"}, status=status.HTTP_400_BAD_REQUEST)

        # Create an instance of the serializer to get the fields
        serializer = serializer_class()
        fields = {}
        for field_name, field in serializer.fields.items():
            if field_name not in ['id', 'created_at', 'updated_at', 'user']:
                fields[field_name] = {
                    "type": field.__class__.__name__,
                    "required": field.required,
                    "help_text": getattr(field, 'help_text', ''),
                    "label": field.label or field_name.replace('_', ' ').capitalize()
                }

                # Add choices for choice fields if available in the model
                model_class = self.get_model_class(item_type)
                if model_class and hasattr(model_class, field_name):
                    model_field = model_class._meta.get_field(field_name)
                    if hasattr(model_field, 'choices') and model_field.choices:
                        fields[field_name]["choices"] = [
                            {"value": choice_value, "display": choice_display}
                            for choice_value, choice_display in model_field.choices
                        ]

        return Response({
            "item_type": item_type,
            "fields": fields
        })

    def post(self, request, item_type):
        """
        Create a new item based on the provided data
        """
        serializer_class = self.get_serializer_class(item_type)
        model_class = self.get_model_class(item_type)

        if not serializer_class or not model_class:
            return Response({"error": "Invalid item type"}, status=status.HTTP_400_BAD_REQUEST)

        # Add the user to the data
        data = request.data.copy()
        data['user'] = request.user.id

        serializer = serializer_class(data=data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TechnicItemCreateView(views.APIView):
    """
    View to create technic items based on the selected category and subcategory
    """

    def get_serializer_class(self, category, subcategory=None):
        """
        Get the appropriate serializer class based on category and subcategory
        """
        serializer_map = {
            "stereo_system": {
                None: StereoSystemSerializer,
                "tv": TVSerializer,
                "monitor": MonitorSerializer
            },
            "pc": {
                None: PCSerializer,
                "cpu": CPUSerializer,
                "gpu": GPUSerializer,
                "ram": RAMSerializer,
                "storage": StorageSerializer
            },
            "console": {
                None: ConsoleSerializer,
                "xbox": XboxSerializer,
                "playstation": PlayStationSerializer,
                "nintendo": NintendoSerializer
            },
            "mobile": {
                None: MobileSerializer
            }
        }

        if category not in serializer_map:
            return None

        if subcategory is not None and subcategory not in serializer_map[category]:
            return None

        return serializer_map[category][subcategory]

    def get_model_class(self, category, subcategory=None):
        """
        Get the appropriate model class based on category and subcategory
        """
        model_map = {
            "stereo_system": {
                None: StereoSystem,
                "tv": TV,
                "monitor": Monitor
            },
            "pc": {
                None: PC,
                "cpu": CPU,
                "gpu": GPU,
                "ram": RAM,
                "storage": Storage
            },
            "console": {
                None: Console,
                "xbox": Xbox,
                "playstation": PlayStation,
                "nintendo": Nintendo
            },
            "mobile": {
                None: Mobile
            }
        }

        if category not in model_map:
            return None

        if subcategory is not None and subcategory not in model_map[category]:
            return None

        return model_map[category][subcategory]

    def get(self, request, category, subcategory=None):
        """
        Get the form fields required for creating a technic item of the selected type
        """
        serializer_class = self.get_serializer_class(category, subcategory)
        model_class = self.get_model_class(category, subcategory)

        if not serializer_class:
            return Response({"error": "Invalid category or subcategory"}, status=status.HTTP_400_BAD_REQUEST)

        # Create an instance of the serializer to get the fields
        serializer = serializer_class()
        fields = {}
        for field_name, field in serializer.fields.items():
            if field_name not in ['id', 'created_at', 'updated_at', 'user'] and not field_name.endswith('_display'):
                fields[field_name] = {
                    "type": field.__class__.__name__,
                    "required": field.required,
                    "help_text": getattr(field, 'help_text', ''),
                    "label": field.label or field_name.replace('_', ' ').capitalize()
                }

                # Add choices for choice fields if available in the model
                if model_class and hasattr(model_class, field_name):
                    model_field = model_class._meta.get_field(field_name)
                    if hasattr(model_field, 'choices') and model_field.choices:
                        fields[field_name]["choices"] = [
                            {"value": choice_value, "display": choice_display}
                            for choice_value, choice_display in model_field.choices
                        ]

        return Response({
            "category": category,
            "subcategory": subcategory,
            "fields": fields
        })

    def post(self, request, category, subcategory=None):
        """
        Create a new technic item based on the provided data
        """
        serializer_class = self.get_serializer_class(category, subcategory)
        model_class = self.get_model_class(category, subcategory)

        if not serializer_class or not model_class:
            return Response({"error": "Invalid category or subcategory"}, status=status.HTTP_400_BAD_REQUEST)

        # Add the user to the data
        data = request.data.copy()
        data['user'] = request.user.id

        serializer = serializer_class(data=data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserItemsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for listing and retrieving user's items
    """
    serializer_class = ItemSerializer

    def get_queryset(self):
        """
        Return items belonging to the authenticated user
        """
        return Item.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        """
        Return appropriate serializer class based on the item type
        """
        # For list action, use the default serializer
        if self.action == 'list':
            return ItemSerializer

        # For retrieve action, get the specific serializer based on the instance type
        if self.action == 'retrieve':
            instance = self.get_object()

            # Map model classes to serializer classes
            serializer_map = {
                Book: BookSerializer,
                Clothes: ClothesSerializer,
                Game: GameSerializer,
                Technic: TechnicSerializer,
                StereoSystem: StereoSystemSerializer,
                PC: PCSerializer,
                Console: ConsoleSerializer,
                Mobile: MobileSerializer,
                TV: TVSerializer,
                Monitor: MonitorSerializer,
                CPU: CPUSerializer,
                GPU: GPUSerializer,
                RAM: RAMSerializer,
                Storage: StorageSerializer,
                Xbox: XboxSerializer,
                PlayStation: PlayStationSerializer,
                Nintendo: NintendoSerializer,
            }

            # Get the real instance class (polymorphic)
            real_instance = instance.get_real_instance_class()

            # Return the appropriate serializer class or default to ItemSerializer
            return serializer_map.get(real_instance, ItemSerializer)

        # Default fallback
        return ItemSerializer
