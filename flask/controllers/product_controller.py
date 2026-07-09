from extensions import app

@app.get('/products')
def get_products():
    return {'status': 'success', 'message': 'Products endpoint...'}