from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/products', methods=['POST'])
def add_product():
  # create product dict
  new_product = request.get_json()

  # read existing products from JSON file
  with open('./db/products.json', 'r') as f:
    products = json.load(f)

  # find new ID for the product
  new_id = 0
  for product in products:
    if product['id'] > new_id:
      new_id = product['id']
  new_id += 1
  new_product['id'] = new_id

  # add product to array
  products.append(new_product)

  # save updated JSON data to file
  with open('./db/products.json', 'w') as f:
    json.dump(products, f, indent=4)

  return new_product, 201

@app.route('/products')
def get_list_products():
  # read existing products from JSON file
  with open('./db/products.json', 'r') as f:
    products = f.read()

  return products, 200

@app.route('/products/<int:id>')
def get_product_details(id):
  # read existing products from JSON file
  with open('./db/products.json', 'r') as f:
    products = json.load(f)
  
  # find product in array
  product = None
  for p in products:
    if p['id'] == id:
      product = p
      break
  else:
    return '', 404

  return jsonify(product), 200

@app.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
  # read existing products from JSON file
  with open('./db/products.json', 'r') as f:
    products = json.load(f)
  
  # find and delete product from array/list
  product = None
  for i, p in enumerate(products):
    if p['id'] == id:
      product = p.copy()
      del products[i]
      break
  else:
    return '', 404

  # save updated JSON data to file
  with open('./db/products.json', 'w') as f:
    json.dump(products, f, indent=4)

  return jsonify(product), 200

if __name__ == '__main__':
  app.run(debug=True)
