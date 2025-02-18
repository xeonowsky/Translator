Translator
Project Description ENG
Translator is an application written in Python that enables text translation between different languages using a translation API.
The application features a GUI created with the wxPython library. The project is simple to use and can be extended with additional functionalities.

Features:
Translation of text between different languages (PL, EN, DE, FR, ES).
Ability to select the source and target languages.
Simple and intuitive graphical user interface.

Technologies:
Language: Python 3.x

Libraries:
requests – for sending HTTP requests
json – for handling API responses

Requirements: To run the project, you will need:
Python 3
API key for the translation service

Installation: Clone the repository:

git clone https://github.com/xeonowsky/Translator.git
Install the required libraries:

pip install wxPython
pip install requests
Then, you need to create an account on DeepL: https://support.deepl.com/hc/en-us at the provided link. After creating an account, you need to obtain an API key, which is generated after filling out the necessary forms. The key is required for the translation request.

After obtaining the key, add it to the code in the appropriate place:

python
api_key = "***PLACE FOR API KEY***"
Run the application and enjoy the translations!
####################################################################################

Translator
Opis projektu PL
Translator to aplikacja napisana w Pythonie, która umożliwia tłumaczenie tekstu między różnymi językami przy użyciu API tłumaczeniowego.
Aplikacja posiada GUI stworzony przy pomocy biblioteki wxPython. Projekt jest prosty w użyciu i może być rozszerzony o dodatkowe funkcjonalności.

Funkcjonalności:
Tłumaczenie tekstu pomiędzy różnymi językami (PL, EN, DE, FR, ES).
Możliwość wyboru języka źródłowego i docelowego.
Prosty i intuicyjny interfejs graficzny.

Technologie
Język: Python 3.x
Biblioteki:
requests – do wysyłania żądań HTTP
json – do obsługi odpowiedzi API


Wymagania
Aby uruchomić projekt, potrzebujesz:
-Python 3
-Klucza API do usługi tłumaczeniowej


Instalacja:
Sklonuj repozytorium:

git clone https://github.com/xeonowsky/Translator.git


Zainstaluj wymagane biblioteki:
pip install wxPython
pip install requests

Następnie potrzebujesz  utworzyć konto na DeepL: https://support.deepl.com/hc/en-us pod podanym linkiem
Po utworzeniu konta potrzebujesz uzyskać klucz do API, który jest generowany po wypełnieniu odpowiednich tam formularzy.
Klucz jest potrzebny do requestu tłumaczenia.
Po uzyskaniu klucza dodajesz go do kodu w odpowiednim miejscu:
api_key = "***PLACE FOR API KEY***"
Uruchom aplikację oraz ciesz się z tłumaczenia
