from mnemonic import Mnemonic
from solana.keypair import Keypair
from base58 import b58encode
import hashlib
from art import tprint

tprint('panicatcks', font='bulbhead')

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
        self.pb = Keypair.from_secret_key(self.seed)
        for i in range(self.number):
            with open(f'{self.filename}_public','a',encoding='utf-8') as pb:
                pb.write(f'{pb}\n')
    def mnemonicphrase(self):
        self.numfile()
        for i in range(self.number):
            self.mnemo = Mnemonic("english")
            self.words = self.mnemo.generate(strength=128)
            with open(f'{self.filename}_mnemonic.txt','a', encoding='utf-8') as mnem:
                mnem.write(f'{self.words}\n')
    def choose(self):
        print('K.Keys\nM.Mnemonic\nP.Public\nE.Exit')
        choose = input('What do you want generate? ').lower()
        if choose == 'k':
            self.privatekeys()
        elif choose == 'm':
            self.mnemonicphrase()
        elif choose == 'p':
            self.public()
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