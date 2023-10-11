# shahry-task

### Extracting Birth date

##### Getting the century

The first digit `x` indicates the century. Using a simple calculation we can obtain the century during which the person was born. If we multiply the first digit by 100 and add 1700, we get the century. `x * 100 + 1700`

##### Getting the year, month and day

the next six digits indicate the year, month and day in the format `YYMMDD`. By extracting this information and adding it to the century we can precisely get the exact birth date.

For example if the first 7 digits are `2960921`. This means the individual is born on 21st September 1996.

### Extracting governorate

There is a very specific mapping where each governorate in Egypt has a specific code.

```
# governerates code mapping
governorates  = {'01': 'Cairo',
'02': 'Alexandria',
'03': 'Port Said',
'04': 'Suez',
'11': 'Damietta',
'12': 'Dakahlia',
'13': 'Ash Sharqia',
'14': 'Kaliobeya',
'15': 'Kafr El - Sheikh',
'16': 'Gharbia',
'17': 'Monoufia',
'18': 'El Beheira',
'19': 'Ismailia',
'21': 'Giza',
'22': 'Beni Suef',
'23': 'Fayoum',
'24': 'El Menia',
'25': 'Assiut',
'26': 'Sohag',
'27': 'Qena',
'28': 'Aswan',
'29': 'Luxor',
'31': 'Red Sea',
'32': 'New Valley',
'33': 'Matrouh',
'34': 'North Sinai',
'35': 'South Sinai',
'88': 'Foreign' }
```

### Extracting Gender

By simply checking if the 13th digit is odd or even we can determine the gender. If odd then the individual is a male, otherwise the individual is a female.

## Checking validity

- length must be exactly 14 characters
- string must be numeric (no alphabets or other characters)
- birthdate must be no later than today's date
- governorate code must be valid

NB: the last digit in the national ID number is a check sum but couldn't find any resources on how it is calculated.
