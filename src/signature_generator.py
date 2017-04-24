#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import hashlib


#Rapport: ceci sert à générer une signature d'un fichier avec md5 selon le contenu du fichier


class SignatureGenerator:
    @staticmethod
    def generate_signature(content):
        utf8_content = content.encode('UTF-8')
        objet_md5 = hashlib.md5()
        objet_md5.update(utf8_content)
        signature = objet_md5.hexdigest()

        return signature
