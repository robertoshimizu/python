#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Você deve criar uma classe carro que vai possuir
dois atributos compostos por outras duas classes:

1) Motor
2) Direção

O Motor terá a responsabilidade de controlar a velocidade.
Ele oferece os seguintes atributos:
1) Atributo de dado velocidade
2) Método acelerar, que deverá incremetar a velocidade de uma unidade
3) Método frear que deverá decrementar a velocidade em duas unidades

A Direção terá a responsabilidade de controlar a direção. Ela oferece
os seguintes atributos:
1) Valor de diração com valores possíveis: Norte, Sul, Leste, Oeste.
2) Método girar_a_direita
2) Método girar_a_esquerda

  N
O   L
  S

    Exemplo:
    >>> # Testando motor
    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.acelerar()
    >>> motor.velocidade
    3
    >>> motor.frear()
    >>> motor.velocidade
    1
    >>> motor.frear()
    >>> motor.velocidade
    0
    >>> # Testando Direcao
    >>> direcao = Direcao()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Norte'
    >>> carro = Carro(direcao, motor)
    >>> carro.motor.velocidade
    0
    >>> carro.motor.acelerar()
    >>> carro.motor.velocidade
    1
    >>> carro.motor.acelerar()
    >>> carro.motor.velocidade
    2
    >>> carro.motor.frear()
    >>> carro.motor.velocidade
    0
    >>> carro.direcao.valor
    'Norte'
    >>> carro.direcao.girar_a_direita()
    >>> carro.direcao.valor
    'Leste'
    >>> carro.direcao.girar_a_esquerda()
    >>> carro.direcao.valor
    'Norte'
    >>> carro.direcao.girar_a_esquerda()
    >>> carro.direcao.valor
    'Oeste'
"""

class Carro:
    def __init__(self, motor, direcao):
        self.motor = Motor()
        self.direcao = Direcao()

class Motor:
    def __init__(self, velocidade=0):
        self.velocidade = velocidade
        
    def velocidade(self):
        return self.velocidade
    
    def acelerar(self):
        self.velocidade +=1
        
    def frear(self):
        self.velocidade -=2
        if self.velocidade < 0:
            self.velocidade = 0

class Direcao:
    def __init__(self,valor='Norte'):
        self.valor = valor
    
    def valor(self):
        return self.valor
    
    def girar_a_direita(self):
        if (self.valor=='Norte'):
            self.valor = 'Leste'
        elif (self.valor=='Leste'):
            self.valor = 'Sul'
        elif (self.valor=='Sul'):
            self.valor = 'Oeste' 
        elif (self.valor=='Oeste'):
            self.valor = 'Norte' 

    def girar_a_esquerda(self):
        if (self.valor=='Norte'):
            self.valor = 'Oeste'
        elif (self.valor=='Oeste'):
            self.valor = 'Sul'
        elif (self.valor=='Sul'):
            self.valor = 'Leste' 
        elif (self.valor=='Leste'):
            self.valor = 'Norte' 
        

