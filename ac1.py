from flask import Flask, request 

app = Flask(__name__) 

@app.route('/') 
def main():
  resultado = 'Entre as notas na URL'    

  primeira = request.args.get('primeira')
  segunda = request.args.get('segunda')

  if primeira and segunda:
        
    primeira = float(primeira)
    segunda = float(segunda)

    media = (primeira + segunda) / 2 

    primeira = str(primeira)
    
    segunda = str(segunda)
    
    resultado = (f"Valor primeira Nota {primeira} <br> Valor Segunda nota  {segunda} <br> Media {media} ")

  return resultado

if __name__ == '__main__':
  app.run(debug=True) 