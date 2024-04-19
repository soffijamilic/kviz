# Kviz
 
## Instaliranje virtualnog okruzenja i flask biblioteke
Kako bi instalirali flask biblioteku u virtualnom okruženju potrebno je pokrenuti sledeću komandu u PowerShell-u iz root foldera:<br>
```
pip install virtualenv
python -m virtualenv env
Set-ExecutionPolicy Unrestricted -Scope Process
.env\Scripts\activate
pip install -r requirements.txt
```

## Instaliranje npm
Iz foldera frontend pokrenuti komandu:

```
npm install
npm run dev
```