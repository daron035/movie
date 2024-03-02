from django.contrib import admin
from django.utils.safestring import mark_safe
from django import forms
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline

from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class MovieAdminForm(forms.ModelForm):
    description = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())

    # description_ru = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())
    # description_en = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())
    class Meta:
        model = Movie
        fields = "__all__"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description", "url")
    list_display_links = ("name",)
    prepopulated_fields = {"url": ("name",)}


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ("name", "get_img")
    readonly_fields = ("get_img",)
    fieldsets = (
        (None, {"fields": (("name", "age", "description"),)}),
        (None, {"fields": (("get_img", "image"),)}),
    )

    def get_img(self, obj):
        return mark_safe(f'<img src={ obj.image.url } width="150">')

    get_img.short_description = "IMAGE"


class ReviewsInline(admin.TabularInline):
    model = Reviews
    extra = 0
    readonly_fields = ("name", "email")


class MovieShotsInline(admin.TabularInline):
    model = MovieShots
    extra = 0
    readonly_fields = ("get_img", "id", "title", "description")
    # fields = ('title', 'movie', 'get_img',)

    def get_img(self, obj):
        return mark_safe(f'<img src={ obj.image.url } width="150">')

    get_img.short_description = mark_safe(f"<strong>Image</strong>")


@admin.register(Movie)
class MovieAdmin(TranslationAdmin):
    list_display = (
        "id",
        "title",
        "age",
        "country",
        "time_create",
        "time_update",
        "is_published",
    )
    # list_display = ('id', 'title')
    list_display_links = ("id", "title")
    search_fields = ("title",)
    list_editable = ("is_published",)
    ordering = ("title",)
    prepopulated_fields = {"url": ("title",)}
    form = MovieAdminForm
    inlines = [MovieShotsInline, ReviewsInline]
    save_on_top = True
    save_as = True
    date_hierarchy = "time_create"
    # fields = ('title', 'actors', 'genre', 'url',)
    readonly_fields = ("get_img",)
    fieldsets = (
        (None, {"fields": (("title", "tagline"),)}),
        (
            None,
            {
                "fields": (
                    "description",
                    ("get_img", "poster"),
                )
            },
        ),
        (None, {"fields": (("age", "country", "world_premiere", "budget"),)}),
        (
            "Staf",
            {
                "classes": ("collapse",),
                "fields": (
                    (
                        "actors",
                        "directors",
                    ),
                ),
            },
        ),
        (None, {"fields": (("genre", "category"),)}),
        (None, {"fields": (("url", "is_published"),)}),
    )

    def get_img(self, obj):
        return mark_safe(f'<img src={ obj.poster.url } width="150">')

    get_img.short_description = mark_safe(f"<strong>Poster</strong>")


# @admin.register(RatingStar)
# class RatingStarAdin(admin.ModelAdmin):


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description", "url")
    list_display_links = ("name",)
    prepopulated_fields = {"url": ("name",)}


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "text", "parent", "movie")
    list_display_links = ("name",)


@admin.register(MovieShots)
class MovieShotsAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "movie",
        "get_img",
    )
    list_display_links = ("movie",)
    readonly_fields = ("get_img", "movie")
    fieldsets = (
        (
            None,
            {
                "fields": (("title", "movie"),),
            },
        ),
        (
            "Image",
            {
                "classes": ("wide", "extrapretty"),
                "fields": (
                    (
                        "get_img",
                        "image",
                    ),
                ),
            },
        ),
        # (None, {
        #     'fields': (('get_img', 'image'), )
        # })
    )
    search_fields = ("movie",)
    list_filter = ("movie",)

    def get_img(self, obj):
        return mark_safe(f'<img src={ obj.image.url } width="150">')

    get_img.short_description = mark_safe(f"<strong>Image</strong>")


admin.site.site_title = "Administration"
admin.site.site_header = "Administration"

# # admin.site.register(Category, CategoryAdmin)
# admin.site.register(Actor)
# # admin.site.register(Genre)
# # admin.site.register(Movie, MovieAdmin)
# admin.site.register(MovieShots)
admin.site.register(Rating)
admin.site.register(RatingStar)
# admin.site.register(Reviews)
