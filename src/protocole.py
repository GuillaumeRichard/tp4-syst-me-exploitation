#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#Rapport: Interface pour les protocoles xml et json


class Protocole:
    """
    Classe représentant le langage de communication avec le serveur.
    """

    server_root = ''

    def __init__(self, server_root):
        self.server_root = server_root
