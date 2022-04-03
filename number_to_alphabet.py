import json

unit = ('', 'هزار و', 'میلیون و', 'میلیارد و', 'بیلیون و', 'تریلیون و', 'کوادریلیون و', 'کوینتیلیون و', 'سیکستیلون و',
        'سپتیلیون و', 'اکتیلیون و', 'نونیلیون و', 'دسیلیون و', 'آندسیلیون و', 'دودسیلیون و', 'تریدسیلیون و',
        'کواتردسیلیون و', 'کویندسیلیون و', 'سیکسدسیلیون و', 'سپتندسیلیون و', 'اکتودسیلیوم و', 'نومدسیلیون و')

with open('alphabets.json') as json_file:
    numbers_alphabet = {int(k): v for k, v in json.load(json_file).items()}


def convert_number_to_alphabet(number):
    if not isinstance(number, int):
        raise TypeError(f"The number argument must be integer not a '{type(number).__name__}'")
    split_number = f'{number:,}'.split(',')
    alphabet_number = ''
    # Receive numbers in order of low to high place value
    for i, item in enumerate(reversed(split_number)):
        alphabet_itm = ''
        if int(item) == 0:
            continue
        elif int(item) in numbers_alphabet:
            alphabet_itm += numbers_alphabet[int(item)]
        else:
            for j, digit in enumerate(item):
                # check place values of tens smaller than 21 or not
                if all((j == 1, int(digit) == 1, int(item[j:]) in numbers_alphabet)):
                    alphabet_itm += ' ' + numbers_alphabet[int(item[j:])]
                    break
                else:
                    num = digit + ('0' * ((len(item) - 1) - j))
                    alphabet_itm += ' ' + numbers_alphabet[int(num)]
        # Replace "و" with "white space"
        alphabet_itm = ' و '.join(alphabet_itm.split())
        # Set the number's alphabet unit
        alphabet_number = ' '.join((alphabet_itm, unit[i], alphabet_number))
    return alphabet_number.strip(' و')
