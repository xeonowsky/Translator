import wx
import requests

class TranslatorApp(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title, size=(600, 400))
        panel = wx.Panel(self)
        source_label = wx.StaticText(panel, label="Tekst do tłumaczenia:")
        self.source_text = wx.TextCtrl(panel, style=wx.TE_MULTILINE)

        target_label = wx.StaticText(panel, label="Przetłumaczony tekst:")
        self.result_text = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY)


        self.source_lang = wx.ComboBox(panel, choices=["PL", "EN", "DE", "FR", "ES"], style=wx.CB_READONLY)
        self.source_lang.SetValue("EN")

        self.target_lang = wx.ComboBox(panel, choices=["PL", "EN", "DE", "FR", "ES"], style=wx.CB_READONLY)
        self.target_lang.SetValue("PL")
        translate_button = wx.Button(panel, label="Tłumacz")
        translate_button.Bind(wx.EVT_BUTTON, self.translate_text)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(source_label, flag=wx.ALL, border=10)
        sizer.Add(self.source_text, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        sizer.Add(target_label, flag=wx.ALL, border=10)
        sizer.Add(self.result_text, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)

        lang_sizer = wx.BoxSizer(wx.HORIZONTAL)
        lang_sizer.Add(wx.StaticText(panel, label="Język źródłowy:"), flag=wx.ALL, border=10)
        lang_sizer.Add(self.source_lang, flag=wx.ALL, border=10)
        lang_sizer.Add(wx.StaticText(panel, label="Język docelowy:"), flag=wx.ALL, border=10)
        lang_sizer.Add(self.target_lang, flag=wx.ALL, border=10)

        sizer.Add(lang_sizer, flag=wx.ALL | wx.CENTER, border=10)
        sizer.Add(translate_button, flag=wx.ALL | wx.CENTER, border=10)

        panel.SetSizer(sizer)
        self.Show()

    def translate_text(self, event):
        text = self.source_text.GetValue().strip()
        source_lang = self.source_lang.GetValue()
        target_lang = self.target_lang.GetValue()

        if not text:
            wx.MessageBox("Proszę wpisać tekst do tłumaczenia.", "Błąd", wx.OK | wx.ICON_ERROR)
            return

        api_key = "***PLACE FOR API KEY***"
        url = "https://api-free.deepl.com/v2/translate"
        params = {
            "auth_key": api_key,
            "text": text,
            "source_lang": source_lang,
            "target_lang": target_lang,
        }

        try:
            response = requests.post(url, data=params)
            response.raise_for_status()
            data = response.json()

            if "translations" in data:
                translation = data["translations"][0]["text"]
                self.result_text.SetValue(translation)
            else:
                wx.MessageBox("Nie udało się przetłumaczyć tekstu.", "Błąd", wx.OK | wx.ICON_ERROR)
        except requests.exceptions.RequestException as e:
            wx.MessageBox(f"Wystąpił błąd: {e}", "Błąd", wx.OK | wx.ICON_ERROR)

if __name__ == "__main__":
    app = wx.App(False)
    frame = TranslatorApp(None, "Tłumacz tekstu")
    app.MainLoop()
