from django.db import models
from django.contrib.auth.models import User

from products.models import Product, Category
from profiles.models import UserProfile


# Constants for Contact Model --------------------------- #
BOARD_TYPE = [
    ("Shortboard", "Shortboard"),
    ("Fishboard", "Fishboard"),
    ("Malibu", "Malibu"),
    ("Funboard", "Funboard"),
    ("Longboard", "Longboard"),
    ("Gun", "Gun"),
]

TAIL_TYPE = [
    ("Swallow", "Swallow"),
    ("Round", "Round"),
    ("Pin", "Pin"),
    ("Square", "Square"),
    ("Squash", "Squash"),
]

SKILL_LEVEL = [
    ("Beginner", "Beginner"),
    ("Beginner Intermediate", "Beginner Intermediate"), 
    ("Intermediate", "Intermediate"),
    ("Advanced", "Advanced"),
    ("Pro", "Pro"),
]

SURF_STYLE = [
    ("Cruising", "Cruising"),
    ("Carving", "Carving"),
    ("Aerials", "Aerials"),
]

WAVE_SIZE = [
    ("Knee", "Knee"),
    ("Waist", "Waist"),
    ("Chest", "Chest"),
    ("Head", "Head"),
    ("Head+", "Head+"),
]

WAVE_POWER = [
    ("Weak", "Weak"),
    ("Medium", "Medium"),
    ("Strong", "Strong"),
]

COLOR_THEME = [
    ("Light", "Light"),
    ("Dark", "Dark"),
]

# Constants for Art Model --------------------------- #
ART = [
    ("None", "None"),
    ("Mandala", "Mandala"),
    ("Flower", "Flower"),
    ("Turtle", "Turtle"),
    ("Whale", "Whale"), 
    ("Octopus", "Octopus"),
    ("Fish", "Fish"),
    ("Waves", "Waves"), 
    ("Abstract", "Abstract"),
    ("Surprise Me", "Surprise Me"),
]

# Models ------------------------------------------------------------ ##
class Art(models.Model):
    """
    Model for art
    """
    class Meta:
        verbose_name = "Decorative Art"
    
    type = models.CharField(max_length=100, choices=ART, null=False, blank=False)


class Contact(models.Model):

    class Meta:
        verbose_name = "Customer Contact"

    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    sent_at = models.DateTimeField(auto_now_add=True)
    message_read = models.BooleanField(default=False)
    subject = models.CharField(max_length=100, null=True, blank=True)
    message = models.TextField(max_length=3000, null=False, blank=False)
    product = models.ForeignKey(
        "Product", on_delete=models.CASCADE, related_name="concerning_product",
        null=True, blank=True
    )
    category = models.ForeignKey(
        "Category", on_delete=models.CASCADE, related_name="concerning_category",
        null=True, blank=True
    )
    board_type = models.CharField(max_length=20, choices=BOARD_TYPE, null=True, blank=True)
    tail = models.CharField(max_length=20, choices=TAIL_TYPE, null=True, blank=True)
    body_height = models.IntegerField(null=True, blank=True)
    body_weight = models.IntegerField(null=True, blank=True)
    board_length = models.IntegerField(null=True, blank=True)
    board_volume = models.IntegerField(null=True, blank=True)
    skill_level = models.CharField(max_length=25, choices=SKILL_LEVEL, null=True, blank=True)
    surf_style = models.CharField(max_length=20, choices=SURF_STYLE, null=True, blank=True)
    wave_size = models.CharField(max_length=20, choices=WAVE_SIZE, null=True, blank=True)
    wave_power = models.CharField(max_length=20, choices=WAVE_POWER, null=True, blank=True)
    color_theme = models.CharField(max_length=20, choices=COLOR_THEME, null=True, blank=True)
    art = models.ForeignKey(
        "Art", on_delete=models.CASCADE, related_name="concerning_art"
    )
    remarks = models.CharField (max_length=200, null=True, blank=True)

    def __str__(self):
        return f"Message from {self.name} - {self.sent_at}"
