from django.forms import ModelForm, ValidationError
from .models import Author, Book


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'birth_date', 'genre']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if "JAMES" in name.upper():
            raise ValidationError("No James allowed")
        return name
    
    def clean_birth_date(self):
        birth_date = self.cleaned_data.get('birth_date')
        if birth_date.year < 1900:
            raise ValidationError("Authors must be born after 1900")
        return birth_date
    
    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        genre = cleaned_data.get('genre')

        if name and genre:
            if name.upper() == "AGATHA CHRISTIE" and genre.lower() != "mystery":
                raise ValidationError("Agatha Christie must write mystery novels.")
        
        return cleaned_data
    
    def save(self, commit=True):
        author = super().save(commit=False)# create an Author instance but don't save to DB yet, just keep in memory
        author.created_by = "Mike"  # set the created_by field to a default value
        if commit:
            author.save()  # now save to the database
        return author
