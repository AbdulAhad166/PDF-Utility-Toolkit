
from django import forms


# Allows users to select multiple files
class MultiFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


# Validates multiple uploaded files
class MultipleFileField(forms.FileField):
    def clean(self, data, initial=None):
        clean = super().clean

        if isinstance(data, (list, tuple)):
            return [clean(file, initial) for file in data]

        return [clean(data, initial)] if data else clean(data, initial)


class MergePDFForm(forms.Form):
    files = MultipleFileField(
        widget=MultiFileInput(attrs={"accept": ".pdf"}),
        help_text="Select two or more PDF files to merge."
    )


class SplitPDFForm(forms.Form):
    file = forms.FileField(
        widget=forms.ClearableFileInput(attrs={"accept": ".pdf"})
    )
    ranges = forms.CharField(
        help_text="e.g., 1-3,5,7-9 (1-based page numbers)"
    )


class ImagesToPDFForm(forms.Form):
    images = MultipleFileField(
        widget=MultiFileInput(attrs={"accept": "image/*"})
    )


class PDFToImagesForm(forms.Form):
    file = forms.FileField(
        widget=forms.ClearableFileInput(attrs={"accept": ".pdf"})
    )


class ExtractImagesForm(forms.Form):
    file = forms.FileField(
        widget=forms.ClearableFileInput(attrs={"accept": ".pdf"})
    )


class LockPDFForm(forms.Form):
    file = forms.FileField(
        widget=forms.ClearableFileInput(attrs={"accept": ".pdf"})
    )
    password = forms.CharField(widget=forms.PasswordInput)


class UnlockPDFForm(forms.Form):
    file = forms.FileField(
        widget=forms.ClearableFileInput(attrs={"accept": ".pdf"})
    )
    password = forms.CharField(widget=forms.PasswordInput)


class PdfToDocxForm(forms.Form):
    pdf_file = forms.FileField(
        widget=forms.ClearableFileInput(attrs={"accept": ".pdf"}),
        help_text="Upload a PDF file to convert into DOCX."
    )
