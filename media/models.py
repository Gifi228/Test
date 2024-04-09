from django.db import models
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _



class Media(models.Model):
    class FileType(models.TextChoices):
        IMAGE = 'image', _("Image")
        VIDEO = 'video', _("Video")
        DOCUMENT = 'document', _("Document")
        GIF = 'gif', _("Gif")
        OTHER = 'other', _("Other")

    file = models.FileField(upload_to='only_medias/',
                            verbose_name=_("File"),
                            validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'webp',
                                                                                   'mp4', 'avi', 'mpeg4', 'mkv',
                                                                                   'pdf', 'doc', 'docx',
                                                                                   'gif'])])
    file_type = models.CharField(max_length=10,
                                 verbose_name=_("File Type"),
                                 choices=FileType.choices)

    class Meta:
        verbose_name = _("Media")
        verbose_name_plural = _("Media")

    def __str__(self):
        return f"Id: {self.id}|Name: {self.file.name.split('/')[-1]}"

    def clean(self):
        if self.file_type not in self.FileType.values:
            raise ValidationError(_("Invalid File Type"))
        elif self.file_type == self.FileType.IMAGE:
            if self.file.name.split('.')[-1] not in ['jpg', 'jpeg', 'png', 'webp']:
                raise ValidationError("Invalid Image File")
        elif self.file_type == self.FileType.VIDEO:
            if self.file.name.split('.')[-1] not in ['avi', 'mp4', 'mov', 'mkv']:
                raise ValidationError("Invalid Video File")
        elif self.file_type == self.FileType.DOCUMENT:
            if self.file.name.split('.')[-1] not in ['pdf', 'doc', 'docx']:
                raise ValidationError("Invalid Document File")


class MediaSettings(models.Model):
    our_banner_text = models.TextField(verbose_name=_("Our Banner Text"))
    product_page_back_image = models.ForeignKey(Media,
                                                on_delete=models.CASCADE,
                                                verbose_name=_("Product Page Back Image"))

    class Meta:
        verbose_name = _("Media Settings")
        verbose_name_plural = _("Media Settings")