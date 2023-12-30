Dim Message, Speak
Message=InputBox("Ponga el texto","Hablador")
Set Speak=CreateObject("sapi.spvoice")

Speak.Speak Message
