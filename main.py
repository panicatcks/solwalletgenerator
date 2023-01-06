from mnemonic import Mnemonic
from solana.keypair import Keypair
from base58 import b58encode
import hashlib
import base58

class WalletGenerator():
    def privatekeys(self):
        self.numfile()
        for i in range(self.number):
            self.mnemo = Mnemonic("english")
            self.words = self.mnemo.generate(strength=128)
            self.seed = self.mnemo.to_seed(self.words)
            self.keypair = Keypair.from_seed(hashlib.sha256(self.words.encode("utf-8")).digest())
            self.keypair = b58encode(self.keypair.secret_key).decode("utf-8")
            with open(f'{self.filename}_privatekeys.txt','a', encoding='utf-8') as file:
                file.write(f'{self.keypair}\n')
    def public(self):
        self.numfile()
        for i in range(self.number):
            self.mnemo = Mnemonic("english")
            self.words = self.mnemo.generate(strength=128)
            self.seed = self.mnemo.to_seed(self.words)
            self.keypair = Keypair.from_seed(hashlib.sha256(self.words.encode("utf-8")).digest())
            self.keypair = b58encode(self.keypair.secret_key).decode("utf-8")
            self.pb = Keypair.from_secret_key(base58.b58decode(self.keypair))
            self.pb = format(self.pb.public_key)
            with open(f'{self.filename}_public.txt','a',encoding='utf-8') as pb:
                pb.write(f'{self.pb}\n')
    def mnemonicphrase(self):
        self.numfile()
        for i in range(self.number):
            self.mnemo = Mnemonic("english")
            self.words = self.mnemo.generate(strength=128)
            with open(f'{self.filename}_mnemonic.txt','a', encoding='utf-8') as mnem:
                mnem.write(f'{self.words}\n')
    def all(self):
        self.numfile()
        for i in range(self.number):
            self.mnemo = Mnemonic("english")
            self.words = self.mnemo.generate(strength=128)
            self.seed = self.mnemo.to_seed(self.words)
            self.keypair = Keypair.from_seed(hashlib.sha256(self.words.encode("utf-8")).digest())
            self.keypair = b58encode(self.keypair.secret_key).decode("utf-8")
            self.pb = Keypair.from_secret_key(base58.b58decode(self.keypair))
            self.pb = format(self.pb.public_key)
            with open(f'{self.filename}_privatekeys.txt','a', encoding='utf-8') as file:
                file.write(f'{self.keypair}\n')
            with open(f'{self.filename}_mnemonic.txt','a', encoding='utf-8') as mnem:
                mnem.write(f'{self.words}\n')
            with open(f'{self.filename}_public.txt','a',encoding='utf-8') as pb:
                pb.write(f'{self.pb}\n')
    def choose(self):
        print('K.Keys\nM.Mnemonic\nP.Public\nA.ALL\nE.Exit')
        choose = input('What do you want generate? ').lower()
        if choose == 'k':
            self.privatekeys()
        elif choose == 'm':
            self.mnemonicphrase()
        elif choose == 'p':
            self.public()
        elif choose == 'a':
            self.all()
        elif choose == 'e':
            pass
        else:
            print('-'*30)
            print('Wrong choose')
            print('-'*30)
            self.choose()
            pass
    def numfile(self):
        self.number = int(input('Number of wallets '))
        self.filename = input('Name of file ')


def main():
    WalletGenerator().choose()

if __name__ == '__main__':
    main()
