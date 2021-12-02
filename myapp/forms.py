from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django import forms
from .models import Snippet

class SnippetForm(forms.ModelForm):

    class Meta:
        model = Snippet
        fields = ('name', 'email', 'quantity','description', 'sample_type', 'extraction_method',
         'sample_cleanup', 'analysis_instrumentation','analysis_pah','analysis_alkanes','analysis_phenols', 'analysis_tph', 'analysis_btex',
         'log_comments')
        labels = {'name':'Client Name', 'analysis_pah':'PAHs', 'analysis_alkanes':'Alkanes','log_comments': 'Comments',
         'analysis_phenols': 'Phenols','analysis_tph': 'TPH','analysis_tph':'BTEX'}   

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper
        self.helper.form_method = 'post'

        self.helper.layout = Layout(
            'name',
            'email',
            'quantity',
            'description',
            'sample_type',
            'extraction_method',
            'sample_cleanup',
            'analysis_instrumentation',
            'analysis_pah', 
            'analysis_alkanes',
            'analysis_phenols',
            'analysis_tph',
            'analysis_btex',
            'log_comments',
            Submit('submit', 'Submit', css_class='btn-success')
        )