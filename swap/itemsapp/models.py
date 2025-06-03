from django.db import models
from django.conf import settings
from polymorphic.models import PolymorphicModel
from .choice import (Rarity, Book_genre_choice, Clothes_size_choice,
                    Clothes_type_choice, Game_platform_choice,
                    Game_genre_choice, Screen_size_choice, PC_form_factor_choice,
                    Screen_type_choice, Operation_system_choice, Tech_hardware_choices,
                    Xbox_console_choice, PlayStation_console_choice, Nintendo_console_choice,
                    Ram_architecture_choice, Winchester_type_choice)

class Item(PolymorphicModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='items')
    rarity = models.CharField(choices=Rarity)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.name} ({self.polymorphic_ctype})"

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"


# Top-level item types

class Book(Item):
    GENRE_CHOICES = Book_genre_choice
    author = models.CharField(max_length=255)
    pages = models.IntegerField(default=0)
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES)

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"


class Clothes(Item):
    SIZE_CHOICES = Clothes_size_choice
    TYPE_CHOICES = Clothes_type_choice

    size = models.CharField(max_length=3, choices=SIZE_CHOICES)
    color = models.CharField(max_length=50)
    material = models.CharField(max_length=50)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)

    class Meta:
        verbose_name = "Clothes"
        verbose_name_plural = "Clothes"


class Game(Item):
    PLATFORM_CHOICES = Game_platform_choice
    GENRE_CHOICES = Game_genre_choice
    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES)
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES)
    publisher = models.CharField(max_length=255)
    release_year = models.IntegerField()

    class Meta:
        verbose_name = "Game"
        verbose_name_plural = "Games"


class Technic(Item):
    brand = models.CharField(max_length=100, choices=Tech_hardware_choices)
    model_number = models.CharField(max_length=100, blank=True)
    warranty_months = models.IntegerField(default=12)

    class Meta:
        verbose_name = "Technic"
        verbose_name_plural = "Technics"


# Technic subclasses
class StereoSystem(Technic):
    screen_size = models.FloatField(max_length=50, choices=Screen_size_choice)
    resolution = models.CharField(max_length=50, choices=Screen_type_choice)

    class Meta:
        verbose_name = "TV"
        verbose_name_plural = "TVs"


class PC(Technic):
    form_factor = models.CharField(max_length=50, choices=PC_form_factor_choice)
    operating_system = models.CharField(max_length=50, choices=Operation_system_choice)

    class Meta:
        verbose_name = "PC"
        verbose_name_plural = "PCs"


class Console(Technic):
    Platform = models.CharField(max_length=50, choices=Game_platform_choice)
    storage = models.IntegerField()

    class Meta:
        verbose_name = "Console"
        verbose_name_plural = "Consoles"


class Mobile(Technic):
    storage = models.IntegerField()

    class Meta:
        verbose_name = "Mobile"
        verbose_name_plural = "Mobiles"

class TV(StereoSystem):
    is_smart = models.BooleanField(default=False)


class Monitor(StereoSystem):
    response_time = models.FloatField()
    refresh_rate = models.IntegerField()
    is_gaming = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Monitor"
        verbose_name_plural = "Monitors"


# Second level subclasses - PC Components

class PCComponent(PC):
    manufacturer = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        abstract = True


class CPU(PCComponent):
    """CPU component with specific fields"""
    cores = models.IntegerField()
    frequency = models.FloatField(help_text="Base frequency in GHz")
    socket = models.CharField(max_length=50)

    class Meta:
        verbose_name = "CPU"
        verbose_name_plural = "CPUs"


class GPU(PCComponent):
    """GPU component with specific fields"""
    memory = models.IntegerField(help_text="Memory in GB")
    memory_type = models.CharField(max_length=50, help_text="e.g. GDDR6")
    cooling = models.CharField(max_length=50, help_text="e.g. Air, Liquid")

    class Meta:
        verbose_name = "GPU"
        verbose_name_plural = "GPUs"


class RAM(PCComponent):
    """RAM component with specific fields"""
    capacity = models.IntegerField(help_text="Capacity in GB")
    type = models.CharField(max_length=50, choices=Ram_architecture_choice)
    speed = models.IntegerField(help_text="Speed in MHz")

    class Meta:
        verbose_name = "RAM"
        verbose_name_plural = "RAMs"


class Storage(PCComponent):
    """Storage component with specific fields"""
    capacity = models.IntegerField(help_text="Capacity in GB")
    interface = models.CharField(max_length=50, choices=Winchester_type_choice)

    class Meta:
        verbose_name = "Storage"
        verbose_name_plural = "Storage Devices"


# Second level subclasses - Console subclasses

class Xbox(Console):
    """Xbox console with specific fields"""
    model = models.CharField(max_length=50, choices=Xbox_console_choice)

    class Meta:
        verbose_name = "Xbox"
        verbose_name_plural = "Xbox Consoles"


class PlayStation(Console):
    """PlayStation console with specific fields"""
    model = models.CharField(max_length=50, choices=PlayStation_console_choice)

    class Meta:
        verbose_name = "PlayStation"
        verbose_name_plural = "PlayStation Consoles"


class Nintendo(Console):
    model = models.CharField(max_length=50, choices=Nintendo_console_choice)

    class Meta:
        verbose_name = "Nintendo"
        verbose_name_plural = "Nintendo Consoles"
