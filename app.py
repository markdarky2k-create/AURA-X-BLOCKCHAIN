import os
from flask import Flask, jsonify, request, render_template
from blockchain import Blockchain

app = Flask(__name__)
chain = Blockchain()

@app.get('/')
def home():
    return render_template('index.html')

@app.get('/api/status')
def status():
    return jsonify({
        'name': 'AURA-X Blockchain Demo',
        'status': 'running',
        'network': 'AURA-X Demo Network',
        'warning': 'Educational demo only; no real cryptocurrency value.',
        'endpoints': ['/api/chain', '/api/mine', '/api/transaction', '/api/validate', '/api/supply']
    })

@app.get('/api/chain')
def get_chain():
    return jsonify(chain.to_dict())

@app.get('/api/supply')
def supply():
    return jsonify(chain.supply_info())

@app.get('/api/validate')
def validate():
    return jsonify({'valid': chain.is_valid()})

@app.post('/api/transaction')
def transaction():
    data = request.get_json(silent=True) or {}
    sender = str(data.get('sender', '')).strip()
    recipient = str(data.get('recipient', '')).strip()
    amount = data.get('amount')
    if not sender or not recipient or not isinstance(amount, int) or amount <= 0:
        return jsonify({'error': 'sender, recipient and positive integer amount required'}), 400
    chain.add_transaction(sender, recipient, amount)
    return jsonify({'message': 'Transaction added to pending pool', 'pending': chain.pending_transactions})

@app.post('/api/mine')
def mine():
    data = request.get_json(silent=True) or {}
    miner = str(data.get('miner', 'demo-miner')).strip() or 'demo-miner'
    return jsonify(chain.mine_pending(miner))

@app.get('/health')
def health():
    return jsonify({'ok': True})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', '8000'))
    app.run(host='0.0.0.0', port=port, debug=False)
