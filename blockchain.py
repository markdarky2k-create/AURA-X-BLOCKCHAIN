from datetime import datetime, timezone
import hashlib
import json

class Blockchain:
    def __init__(self):
        self.chain = [self._make_block(0, [], '0')]
        self.pending_transactions = []
        self.mining_reward = 10

    @staticmethod
    def _hash_block(block):
        raw = json.dumps(block, sort_keys=True, separators=(',', ':')).encode()
        return hashlib.sha256(raw).hexdigest()

    def _make_block(self, index, transactions, previous_hash):
        block = {
            'index': index,
            'timestamp': datetime.now(timezone.utc).isoformat(),
            'transactions': transactions,
            'previous_hash': previous_hash,
        }
        block['hash'] = self._hash_block(block)
        return block

    def add_transaction(self, sender, recipient, amount):
        self.pending_transactions.append({'sender': sender, 'recipient': recipient, 'amount': amount})

    def mine_pending(self, miner):
        transactions = list(self.pending_transactions)
        transactions.append({'sender': 'AURA-X Network', 'recipient': miner, 'amount': self.mining_reward})
        previous = self.chain[-1]['hash']
        block = self._make_block(len(self.chain), transactions, previous)
        self.chain.append(block)
        self.pending_transactions = []
        return block

    def is_valid(self):
        for i, block in enumerate(self.chain):
            if block['hash'] != self._hash_block({k: block[k] for k in ('index','timestamp','transactions','previous_hash')}):
                return False
            if i > 0 and block['previous_hash'] != self.chain[i-1]['hash']:
                return False
        return True

    def to_dict(self):
        return {'length': len(self.chain), 'chain': self.chain, 'pending_transactions': self.pending_transactions}

    def supply_info(self):
        mined = sum(tx.get('amount', 0) for b in self.chain for tx in b.get('transactions', []) if tx.get('sender') == 'AURA-X Network')
        return {'total_mined_demo_units': mined, 'mining_reward': self.mining_reward}
