#!/usr/bin/env vpython3
# *-* coding: utf-8 *-*
from endesive import pdf


def main():
    
    trusted_cert_pems = (
        # certum chain
        open('ca-certum.pem', 'rt').read(),
        open('ca-ncc.pem', 'rt').read(),
        # actalis chain
        open('ca-actalis-cag1.pem', 'rt').read(),
        open('ca-actalis.pem', 'rt').read(),
        # demo ca chain
        open('demo2_ca.crt.pem', 'rt').read(),
        # demo hsm ca chain
        #open('cert-hsm-ca.pem', 'rt').read(),
    )

    #list of files we want to try
    for fname in (
        'sample-signed.pdf',
    ):
        print('*' * 5, fname,'*' * 5)
        try:
            data = open(fname, 'rb').read()
        except:
            continue
        try:
          (hashok, signatureok, certok) = pdf.verify(data, trusted_cert_pems)
          print('The Signature:', signatureok)
          print('The Hash:', hashok)
          print('The Certificate:', certok)
        except:
          print("The Document is not valid")

      


main()
