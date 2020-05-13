# ######################################################################
# UNIVERSIDADE FEDERAL DE CATALÃO (UFCat)
# DEPARTAMENTO DE ENGENHARIA CIVIL & DEPARTAMENTO DE CIÊNCIAS DA COMPUTAÇÃO
# Autores
# Eduardo Veloso Manhães Seabra 
# Euller Santos Miranda
# Colaboradores
# Wanderlei Malaquias Pereira Junior
# ######################################################################

# Nome: Funções da classe PSO
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
# O programa abaixo contém todas as funções da classe Swarm ou Enxame
#
# ----------

# ---------- Variáveis e suas descrições
#
# Escalares
#
# xvarmin           - Valor inferior do intervalo
# xvarmax           - Valor superior do intervalo
# npop              - Número de população do enxame
# ngen              - Número de gerações da população
# nrep              - número de repetições realizadas
# parada            - Critério de parada do algoritmo
# tFO               - Escolha do tipo de FO utilizado
# tInitPop          - Define o método de inicialização da população
#
# Listas e Vetores:
#
# xvar              - Posição de cada partícula no espaço (Lista de objeto da classe ''Partícula'')
#
# Matrizes e Objetos:
#
#
# ----------

# ---------- Chamada de bibliotecas
#
#
# ----------

# ---------- Chamada de funções ou classes
#
from .Enxame import Enxame
#
# ----------

#
#
# =========================================================================%
# STEP 1: CRIAÇÃO DA CLASSE PSO
# =========================================================================%
#
#
# Step 1.1: Criando a classe Swarm
class PSO(Enxame):

#
#
# =========================================================================%
# STEP 2: MÉTODOS DA CLASSE
# =========================================================================%
#
#
# Step 2.1: Função que cria a velocidade inicial de todas as partículas
    def init_vel_rand(self):
        for i in range(0, self.npop):
            x = []
            for j in range(0, self.nvar):
                x.append(self.calc_rand_intervalos(self.velmax[j], self.velmin[j]))
            self.enxameXvar[i].velocidade = x
    
#
#
# =========================================================================%
# STEP 2: CONSTRUTOR DA CLASSE 
# =========================================================================%
#
#
# Step 2.1: Método construtor da classe
    
    def __init__(self, c1, c2, w, xvarmax:list, xvarmin:list, npop, ngen, nrep, nvar, tInitPop, tFO, parada):
        super().__init__(xvarmax, xvarmin, npop, ngen, nrep, nvar, tFO, parada)
        self.c1                 = c1
        self.c2                 = c2
        self.w                  = w
        self.velmin             = []
        self.velmax             = []
        self.tInitPop           = tInitPop

#
#
# =========================================================================%
# STEP 3: INÍCIO DO PROCEDIMENTO DE OTIMIZAÇÃO
# =========================================================================%
#
#         
# Step 3.1:        
        for rep in range(self.nrep):
            self.limpeza_particula()
            self.velmin.clear()
            self.velmax.clear()
            self.historico_fo.clear()
            self.historico_fit.clear()
            
            for i in range(0, self.nvar):
                self.velmax.append((xvarmax[i]-xvarmin[i])/2)
                self.velmin.append((xvarmin[i]-xvarmax[i])/2)
                

            print("-------------------------")
            print("Início da Repetição: "+str(rep +1))
            print("-------------------------\n")
#
#
# =========================================================================%
# STEP 2: CRIAÇÃO DA POPULAÇÃO INICIAL E CALCULO DE FO E FIT
# =========================================================================%
#
#        
# Step 2.1: Cria a população inicial
            if tInitPop == 1:
                self.init_pop_rand()
                self.init_vel_rand()
            elif tInitPop == 2:
                #Critério Opposite
                0
            else:
                #Erro
                0
# Step 2.2: Calcular valor da função objetivo e da aptidão de cada partícula
            for k in range(0,self.npop):
                self.enxameXvar[k].pessoal_fo = self.enxameXvar[k].fo_cont()
                self.enxameXvar[k].pessoal_fit = self.enxameXvar[k].fit_cont()
                for i in range(0, self.nvar):
                    self.enxameXvar[k].pessoal_xbest.append(self.enxameXvar[k].xvar[i])
# Step 2.3: Verifica a velocidade inicial de cada partícula            
            
            print("Intervalo da velocidade inicial: \n")
            print(self.velmin)
            print(self.velmax)
            
# Step 2.4: Definição do critério de parada do algoritmo
            if(parada=="gerações"):
                cont = 0
                print("\n")
                print("Geração: "+str(cont))
                for k in range(0,self.npop):                
                    print(self.enxameXvar[k])
                    
# Step 2.3: Calcular valor da melhor posição global do enxame
            self.calc_global_best(0)
            self.print_global()
#
#
# =========================================================================%
# STEP 3: PROCESSO ITERATIVO DAS GERAÇÕES
# =========================================================================%
#
#
# Step 3.1: Início do processo iterativo 
            while(cont != self.ngen):
                cont = cont + 1 
                print("gBest: ")
                print(self.global_best)
                print("------------------------------------")
                print("Geração: "+str(cont))
                for k in range(0,self.npop):                
                    print(self.enxameXvar[k])
                    print("pBest: ")
                    print(self.enxameXvar[k].pessoal_xbest)
                    self.enxameXvar[k].mov_PSO(self.c1, self.c2, self.w, self.global_best, \
                                               self.xvarmax, self.xvarmin, \
                                               self.velmax, self.velmin)
                    self.enxameXvar[k].calc_pessoal_xbest
                self.print_global()
                self.list_fo()

#
#
# =========================================================================%
# STEP 3: MÉTODOS DE IMPRESSÃO DE DADOS DO PSO
# =========================================================================%
#
#   