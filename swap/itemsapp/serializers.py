from rest_framework import serializers
from .models import (
    Item, Book, Clothes, Game, Technic,
    StereoSystem, PC, Console, Mobile,
    TV, Monitor,
    CPU, GPU, RAM, Storage,
    Xbox, PlayStation, Nintendo
)


# Base serializer for all items
class ItemSerializer(serializers.ModelSerializer):
    rarity_display = serializers.CharField(source='get_rarity_display', read_only=True)

    class Meta:
        model = Item
        fields = ['id', 'name', 'description', 'price', 'created_at', 'updated_at',
                  'rarity', 'rarity_display', 'quantity', 'user']
        read_only_fields = ['created_at', 'updated_at']


# Top-level item serializers
class BookSerializer(ItemSerializer):
    genre_display = serializers.CharField(source='get_genre_display', read_only=True)

    class Meta(ItemSerializer.Meta):
        model = Book
        fields = ItemSerializer.Meta.fields + ['author', 'pages', 'genre', 'genre_display']


class ClothesSerializer(ItemSerializer):
    size_display = serializers.CharField(source='get_size_display', read_only=True)
    type_display = serializers.CharField(source='get_type_display', read_only=True)

    class Meta(ItemSerializer.Meta):
        model = Clothes
        fields = ItemSerializer.Meta.fields + ['size', 'size_display', 'color', 'material',
                                               'type', 'type_display']


class GameSerializer(ItemSerializer):
    platform_display = serializers.CharField(source='get_platform_display', read_only=True)
    genre_display = serializers.CharField(source='get_genre_display', read_only=True)

    class Meta(ItemSerializer.Meta):
        model = Game
        fields = ItemSerializer.Meta.fields + ['platform', 'platform_display', 'genre',
                                               'genre_display', 'publisher', 'release_year']


class TechnicSerializer(ItemSerializer):
    class Meta(ItemSerializer.Meta):
        model = Technic
        fields = ItemSerializer.Meta.fields + ['brand', 'model_number', 'warranty_months']


# Technic subclass serializers
class StereoSystemSerializer(TechnicSerializer):
    screen_size_display = serializers.CharField(source='get_screen_size_display', read_only=True)
    resolution_display = serializers.CharField(source='get_resolution_display', read_only=True)

    class Meta(TechnicSerializer.Meta):
        model = StereoSystem
        fields = TechnicSerializer.Meta.fields + ['screen_size', 'screen_size_display',
                                                  'resolution', 'resolution_display']


class PCSerializer(TechnicSerializer):
    form_factor_display = serializers.CharField(source='get_form_factor_display', read_only=True)
    operating_system_display = serializers.CharField(source='get_operating_system_display', read_only=True)

    class Meta(TechnicSerializer.Meta):
        model = PC
        fields = TechnicSerializer.Meta.fields + ['form_factor', 'form_factor_display',
                                                  'operating_system', 'operating_system_display']


class ConsoleSerializer(TechnicSerializer):
    platform_display = serializers.CharField(source='get_Platform_display', read_only=True)

    class Meta(TechnicSerializer.Meta):
        model = Console
        fields = TechnicSerializer.Meta.fields + ['Platform', 'platform_display', 'storage']


class MobileSerializer(TechnicSerializer):
    brand_display = serializers.CharField(source='get_brand_display', read_only=True)

    class Meta(TechnicSerializer.Meta):
        model = Mobile
        fields = TechnicSerializer.Meta.fields + ['brand', 'brand_display', 'storage']


# StereoSystem subclass serializers
class TVSerializer(StereoSystemSerializer):
    class Meta(StereoSystemSerializer.Meta):
        model = TV
        fields = StereoSystemSerializer.Meta.fields + ['brand', 'is_smart']


class MonitorSerializer(StereoSystemSerializer):
    class Meta(StereoSystemSerializer.Meta):
        model = Monitor
        fields = StereoSystemSerializer.Meta.fields + ['response_time', 'refresh_rate', 'is_gaming']


# PC component serializers
class CPUSerializer(PCSerializer):
    class Meta(PCSerializer.Meta):
        model = CPU
        fields = PCSerializer.Meta.fields + ['manufacturer', 'model', 'cores', 'frequency', 'socket']


class GPUSerializer(PCSerializer):
    class Meta(PCSerializer.Meta):
        model = GPU
        fields = PCSerializer.Meta.fields + ['manufacturer', 'model', 'memory', 'memory_type', 'cooling']


class RAMSerializer(PCSerializer):
    type_display = serializers.CharField(source='get_type_display', read_only=True)

    class Meta(PCSerializer.Meta):
        model = RAM
        fields = PCSerializer.Meta.fields + ['manufacturer', 'model', 'capacity', 'type',
                                             'type_display', 'speed']


class StorageSerializer(PCSerializer):
    interface_display = serializers.CharField(source='get_interface_display', read_only=True)

    class Meta(PCSerializer.Meta):
        model = Storage
        fields = PCSerializer.Meta.fields + ['manufacturer', 'model', 'capacity', 'interface',
                                             'interface_display']


# Console subclass serializers
class XboxSerializer(ConsoleSerializer):
    model_display = serializers.CharField(source='get_model_display', read_only=True)

    class Meta(ConsoleSerializer.Meta):
        model = Xbox
        fields = ConsoleSerializer.Meta.fields + ['model', 'model_display']


class PlayStationSerializer(ConsoleSerializer):
    model_display = serializers.CharField(source='get_model_display', read_only=True)

    class Meta(ConsoleSerializer.Meta):
        model = PlayStation
        fields = ConsoleSerializer.Meta.fields + ['model', 'model_display']


class NintendoSerializer(ConsoleSerializer):
    model_display = serializers.CharField(source='get_model_display', read_only=True)

    class Meta(ConsoleSerializer.Meta):
        model = Nintendo
        fields = ConsoleSerializer.Meta.fields + ['model', 'model_display']
