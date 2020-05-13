# ######################################################################
# UNIVERSIDADE FEDERAL DE CATALÃO (UFCat)
# DEPARTAMENTO DE ENGENHARIA CIVIL & DEPARTAMENTO DE CIÊNCIAS DA COMPUTAÇÃO
# Autores
# Eduardo Veloso Manhães Seabra 
# Euller Santos Miranda
# Colaboradores
# Wanderlei Malaquias Pereira Junior
# ######################################################################

# Nome: Funções da classe Particula
# Versão:  
# Notas:
# 01-04-20 - E. V. M. Seabra e E. S. Miranda finalizaram a versão beta
# 22-04-20 - E. V. M. Seabra e E. S. Miranda adicionaram o cálculo do FO
#
#
#
#
# ----------

# ---------- Descrição do programa
#
# O programa abaixo contém todas as funções da classe Particula
#
# ----------

# ---------- Variáveis e suas descrições
#
# Escalares:
#
# fo                - Valor da Função Objetivo
# fit               - Valor da Função Aptidão 
# pos               - Indexador da posição da partícula
# pessoal_fo        - Melhor Valor da Função Objetivo para o histórico da Partícula
# pessoal_fit       - Melhor Valor da Função Aptidão para o histórico da Partícula
# tFO               - Escolha do tipo de FO utilizado
#
# Listas e Vetores:
#
# xvar              - Posição das Partículas no espaço n dimensional
# velocidade        - Velocidade das Partículas no espaço n dimensional
# pessoal_xbest     - Melhor valor de Posição para o histórico da Partícula
#
# Matrizes e Objetos:
#
#
# ----------

# ---------- Chamada de bibliotecas
#
import random
#
# ----------

# ---------- Chamada de funções ou classes
#
#
#
# ----------

#
#
# =========================================================================%
# STEP 1: CRIAÇÂO DA CLASSE PARTÍCULA
# =========================================================================%
#
#
class Particula:
    
#
#
# =========================================================================%
# STEP 2: CONSTRUTOR DA CLASSE
# =========================================================================%
#
#
# Step 2.1: Método construtor da classe
    def __init__(self, xvar:list, pos, tFO):
        self.xvar               = xvar
        self.velocidade         = []
        self.fo                 = 0
        self.fit                = 0
        self.pessoal_xbest      = []
        self.pessoal_fo         = 0
        self.pessoal_fit        = 0
        self.tFO                = tFO
        self.pos                = pos
        self.nafo               = 0
        self.historico_p_xbest  = []

#
#
# =========================================================================%
# STEP 3: MÉTODOS DE OPERAÇÃO DA FUNÇÃO OBJETIVO E APTIDÃO
# =========================================================================%
#
#
# Step 3.1: Cálcula a função objetivo

    def fo_cont(self):
        fo = 0
        print("\n\n\n")
        print(self.xvar)
        for i in range(len(self.xvar)):

# Step 3.1.1: Função Sphere
            if(self.tFO == "sphere"):             
                fo += pow(self.xvar[i],2)
            if(self.tFO == "algo"):
                0
        self.fo     = fo
        self.nafo   += 1
        return self.fo
        
# Step 3.2: Cálcula a função aptidão da partícula para valores contínuos
    def fit_cont(self):
        if (self.fo > 0):
            self.fit = 1/(1+self.fo)
            return self.fit
        else:
            self.fit = 1+abs(self.fo)
            return self.fit

#
#
# =========================================================================%
# STEP 4: MÉTODOS DE MOVIMENTAÇÃO PARA O PSO
# =========================================================================%
#
#
# Step 4.1: Movimento da partícula para o PSO e verificação dos limites
    def mov_PSO(self,perSetup1, perSteup2, inertia, global_best, \
                xvarmax, xvarmin, velmax, velmin):

# Step 4.1.1: Atribuição de valores do front-end via personalSetup
        w = inertia
        c1 = perSetup1
        c2 = perSteup2

# Step 4.1.2: Laço para movimento da velocidade e posição
        for i in range(len(self.xvar)):

# Step 4.1.3: Movimento da velocidade
            termo_cognitivo     = c1 * random.random() * (self.pessoal_xbest[i] - self.xvar[i])
            termo_social        = c2 * random.random() * (global_best[i] - self.xvar[i])
            self.velocidade[i]  = (w * self.velocidade[i]) + termo_cognitivo + termo_social

# Step 4.1.4: Verificação do limite de velocidade
            if(self.velocidade[i]>velmax[i]):
                self.velocidade[i] = velmax[i]
            if(self.velocidade[i]<velmin[i]):
                self.velocidade[i] = velmin[i]

# Step 4.1.5: Movimento da posição da partícula            
            self.xvar[i] = self.xvar[i]+self.velocidade[i]
            
# Step 4.1.6: Verificação do limite da posição
            if(self.xvar[i]>xvarmax[i]):
                self.xvar[i] = xvarmax[i]
            if(self.xvar[i]<xvarmin[i]):
                self.xvar[i] = xvarmin[i]
# Step 4.1.7 Cálcula a nova função objetivo
        self.fo_cont()

# Step 4.1.8 Cálcula a nova aptidão
        self.fit_cont()

# Step 4.2: Setar a velocidade inicial
    def set_velocidade(self, velocidade):
        self.velocidade = velocidade

#
#
# =========================================================================%
# STEP 5: MÉTODOS DE PARA AVALIAÇÃO DO HISTÓRICO DA PARTÍCULA
# =========================================================================%
#
#  
# Step 5.1 Muda a melhor posição da partícula caso a aptidão seja maior
    
    def calc_pessoal_xbest(self, tempFit):
        if(tempFit>self.pessoal_fit):
            self.pessoal_fit = tempFit
            self.pessoal_fo = self.fo
            self.pessoal_xbest = self.xvar


# ---------------------------------------------------------------------

         
#
#
# =========================================================================%
# STEP 6: MÉTODOS DE IMPRESSÃO DE DADOS DA PARTÍCULA
# =========================================================================%
#
#          


# Step 6.1: Impressão de dados da partícula
    def __str__(self):
        x = "\nPosição da partícula: " + str(self.pos+1)  +"\n"  +str(self.xvar) + \
            "\nFunção objetivo\n" + str(self.fo) + \
            "\nAptidão\n" + str(self.fit)
        return x
        
        
    
    
