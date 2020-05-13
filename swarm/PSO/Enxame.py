# ######################################################################
# UNIVERSIDADE FEDERAL DE CATALÃO (UFCat)
# DEPARTAMENTO DE ENGENHARIA CIVIL & DEPARTAMENTO DE CIÊNCIAS DA COMPUTAÇÃO
# Autores
# Eduardo Veloso Manhães Seabra 
# Euller Santos Miranda
# Colaboradores
# Wanderlei Malaquias Pereira Junior
# ######################################################################

# Nome: Funções da classe Enxame
# Versão:  v01
# Notas:
# 01-04-20 - E. V. M. Seabra e E. S. Miranda finalizaram a versão beta
#
#
#
#
# ----------

# ---------- Descrição do programa
#
# O programa abaixo contém todas as funções da classe Enxame
#
# ----------

# ---------- Variáveis e suas descrições
#
# Escalares
#
# xvarmin          - Valor inferior do intervalo
# xvarmax          - Valor superior do intervalo
# metodootimizacao - Usuário pode escolher o método de otimização utilizado
# npop             - Número de população do enxame
# ngen             - Número de gerações da população
# nrep             - número de repetições realizadas
# tFO               - Escolha do tipo de FO utilizado
#
# Listas e Vetores:
#
# xvar             - Posição de cada partícula no espaço (Lista do objeto da classe ''particle'')
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
from .Particula import Particula
#
# ----------



#
#
# =========================================================================%
# STEP 1: CRIAÇÃO DA CLASSE ENXAME
# =========================================================================%
#
#
# Step 1.1: Criando a classe Enxame
class Enxame:
    
#
#
# =========================================================================%
# STEP 2: CONSTRUTOR DA CLASSE
# =========================================================================%
#
#
# Step 2.1: Função construtora da classe
    def __init__(self, xvarmax:list, xvarmin:list, npop, ngen, nrep, nvar, tFO, parada):
        self.xvarmax            = xvarmax
        self.xvarmin            = xvarmin
        self.npop               = npop
        self.ngen               = ngen
        self.nrep               = nrep
        self.nvar               = nvar
        self.tFO                = tFO
        self.parada             = "gerações"
        self.enxameXvar         = []
        self.global_best        = []
        self.global_fo          = 0
        self.global_fit         = 0
        self.historico_fo       = []
        self.historico_fit      = []
        self.nafo               = 0

#
#
# =========================================================================%
# STEP 3: MÉTODOS DE CONSTRUÇÃO DA POPULAÇÃO INICIAL
# =========================================================================%
#
#
# Step 3.1: Função que cria a posição inicial de todas as partículas      
    def init_pop_rand(self):
        for i in range(0, self.npop):
            x = []
            for j in range(0, self.nvar):
                x.append(self.calc_rand_intervalos(self.xvarmin[j], self.xvarmax[j]))
            self.enxameXvar.append(Particula(x, i, self.tFO))            
                

        
# Step 3.3: Função que cria pontos randômicos dentro de um intervalo definido               
    def calc_rand_intervalos(self, vMin, vMax):
        r = random.random()
        print("Randomico:"+str(r))
        x0 = (vMin + (vMax - vMin) * r)
        print(x0)
        return x0
#        return [self.xvarmin[j] + (self.xvarmax[j] - self.xvarmin[j]) * \
#             r for j in range(0,self.nvar)]

#
#
# =========================================================================%
# STEP 4: MÉTODO DE DETERMINAÇÃO DA MELHOR PARTÍCULA DO ENXAME
# =========================================================================%
#
#
# Step 4.1: Calculando o melhor posição(xvar) de todo enxame
    def calc_global_best(self, gen):
        if(gen==0):
            tempFit = -1
        else:
            tempFit = self.global_fit        
        for i in range(0, self.npop):
                if(self.enxameXvar[i].fit>tempFit):
                    tempFit = self.enxameXvar[i].fit
                    self.global_fo = self.enxameXvar[i].fo
                    self.global_fit = tempFit
                    self.global_best.clear()
                    for j in range(0, self.nvar):
                        self.global_best.append(self.enxameXvar[i].xvar[j])

#
#
# =========================================================================%
# STEP 5: MÉTODOS DE IMPRESSÃO DE DADOS DO ENXAME
# =========================================================================%
#
#    
# Step 5.1: Impressão de dados do Enxame
    def print_global(self):
        print("\nGlobal Best:")
        for j in range(0, self.nvar):
            print("Dim: " + str(j) + " " + str(self.global_best[j]))
        print("Aptidão Global: " + str(self.global_fit))
        print("Função Objetivo Global: " + str(self.global_fo))
        print("\n")
            
    def list_fo(self):
        x = self.global_fo
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        print(x)
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        self.historico_fo.append(x)
        
        


#
#
# =========================================================================%
# STEP 5: LIMPEZA DAS VARIÁVEIS DE PROJETO
# =========================================================================%
#
#
# Step 5.1: Função que limpa a lista de Partículas
    def limpeza_particula(self):
        self.enxameXvar.clear()
        
        
        

      
        
                
    
    
    
    
    
        