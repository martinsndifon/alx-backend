## i18n
i18n stands for "internationalization," and it is a software engineering practice aimed at designing and developing software applications in a way that allows easy adaptation to various languages, cultures, and regions without the need for significant code changes. The term "i18n" comes from the fact that there are 18 letters between the letter "i" and the letter "n" in the word "internationalization."

The goal of internationalization is to create applications that can be easily localized for different languages and regions, making it accessible and user-friendly to people from diverse linguistic and cultural backgrounds. By implementing i18n best practices, developers can separate the application's content (such as strings, messages, and user interface elements) from the code, enabling easy replacement or translation of content based on the user's locale.

Key features of i18n in software development include:

Message Translation: Storing text strings and messages in a separate resource file or database, allowing them to be translated into different languages.

Locale Support: Implementing support for different locales (language and region combinations) to customize the application's behavior and presentation based on the user's preferences.

Date and Time Formats: Adapting date and time formats to match the conventions of different locales (e.g., displaying dates as MM/DD/YYYY in the US and DD/MM/YYYY in the UK).

Number Formats: Adjusting number formats (decimal separators, digit grouping, etc.) to match the conventions of various regions.

Unicode Support: Ensuring that the application can handle and display characters from various writing systems (e.g., Latin, Cyrillic, Chinese, Arabic) through Unicode encoding.

Right-to-Left (RTL) Support: Providing support for RTL languages such as Arabic and Hebrew, where the text and user interface elements are aligned from right to left.

By adopting internationalization principles during software development, developers can create applications that are more accessible and user-friendly to a global audience, fostering better user engagement and international market reach. Once an application is internationalized, the process of adapting it to specific languages and regions is known as "localization" (l10n). Localization involves translating and customizing the application's content and user interface elements for specific target locales.


### Example of parameterizing templates
Create a babel.cfg file containing
```bash
[python: **.py]
[jinja2: **/templates/**.html]
extensions=jinja2.ext.autoescape,jinja2.ext.with_
```
Then initialize your translations with
```bash
$ pybabel extract -F babel.cfg -o messages.pot .
```
and your two dictionaries/languages with
```bash
$ pybabel init -i messages.pot -d translations -l en
$ pybabel init -i messages.pot -d translations -l fr
```
Then edit files `translations/[en|fr]/LC_MESSAGES/messages.po` to provide the correct value for each message ID for each language. Use the following translations:

Then compile your dictionaries/languages with 
```bash
$ pybabel compile -d translations
```
Reload the home page of your app to see the update
