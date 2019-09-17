import re
from django.core.exceptions import ValidationError

from django.forms import ModelForm
from translations.models import Translate


class TransferForm(ModelForm):

    class Meta:
        model = Translate
        fields = ['in_num']

    def validate_number(self):
        try:
            num_str = self.cleaned_data['in_num']
        except KeyError:
            raise ValidationError('Данные должны быть указаны', code=400)

        if num_str.isdigit():
            if not 0 <= int(num_str) <= 3999:
                raise ValidationError(
                    'Число должно быть от 0 до 3999', code=400)
        else:
            number_string = ''.join(num_str.split())
            for char in number_string:
                if char not in "IVXLCDM":
                    raise ValidationError(
                        'Введите действительное Римское число', code=400)
                else:
                    res = re.fullmatch(
                        r'^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$', number_string)
                    if not res:
                        raise ValidationError(
                            'Введите действительное Римское число', code=400)
        return

    def clean(self):
        self.validate_number()
        return super(TransferForm, self).clean()
