from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text', 'author')
        
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
    #
    # class CommentForm(forms.Form):
    # name = forms.CharField(widget=forms.TextInput(attrs={'class': 'special'}))
    # url = forms.URLField()
    # comment = forms.CharField(widget=forms.TextInput(attrs={'size': '40'}))
#
# Django will then include the extra attributes in the rendered output:
#
# >>> f = CommentForm(auto_id=False)
# >>> f.as_table()
# <tr><th>Name:</th><td><input type="text" name="name" class="special" required /></td></tr>
# <tr><th>Url:</th><td><input type="url" name="url" required /></td></tr>
# <tr><th>Comment:</th><td><input type="text" name="comment" size="40" required /></td></tr>
# You can also set the HTML id using attrs. See BoundField.id_for_label for an example.
