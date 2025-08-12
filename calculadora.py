# importando tkinter
from tkinter import *
from tkinter import ttk

#cores

cor1  = "#30302f" #preto
cor2 = "#feffff" #branco
cor3 = "#38576b" #azul
cor4 = "#ECEFF1" #cinza
cor5 = "#FFAB40" #laranja



janela =Tk()
janela.title("calculadora")
janela.geometry("235x318")
janela.config(bg=cor1)


# criando frames 
frame_tela = Frame(janela, width=235, height=50,bg = cor3)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=268,)
frame_corpo.grid(row=1, column=0)

#criando label
# Removido app_label, pois tela já é usada para exibir os valores



# Função para limpar a tela
def limpar():
	global expressao
	expressao = ""
	tela.config(text="")

#criando botoes

b_1 = Button(frame_corpo, text="C", width=11, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, command=limpar)
b_1.place(x=0, y=0)                 
b_2 = Button(frame_corpo, text="%", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, command=lambda: atualizar_tela('%'))
b_2.place(x=118, y=0)   
b_3 = Button(frame_corpo, text="/", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, command=lambda: atualizar_tela('/'))
b_3.place(x=177, y=0)
b_4 = Button(frame_corpo, text="7", width=5, height=2, bg=cor2, fg=cor1, font=('Ivy 13 bold'), relief=RAISED, command=lambda: atualizar_tela('7'))
b_4.place(x=0, y=52)        
b_5 = Button(frame_corpo, text="8", width=5, height=2, bg=cor2, fg=cor1, font=('Ivy 13 bold'), relief=RAISED, command=lambda: atualizar_tela('8'))
b_5.place(x=59, y=52)



b_6 = Button(frame_corpo, text="9", width=5, height=2, bg=cor2, fg=cor1, font=('Ivy 13 bold'), relief=RAISED, command=lambda: atualizar_tela('9'))
b_6.place(x=118, y=52)
b_7 = Button(frame_corpo, text="*", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, command=lambda: atualizar_tela('*'))
b_7.place(x=177, y=52)  
b_8 = Button(frame_corpo, text="4", width=5, height=2, bg=cor2, fg=cor1, font=('Ivy 13 bold'), relief=RAISED, command=lambda: atualizar_tela('4'))
b_8.place(x=0, y=104)   
b_9 = Button(frame_corpo, text="5", width=5, height=2, bg=cor2, fg=cor1, font=('Ivy 13 bold'), relief=RAISED, command=lambda: atualizar_tela('5'))
b_9.place(x=59, y=104)  
b_10 = Button(frame_corpo, text="6", width=5, height=2, bg=cor2, fg=cor1, font=('Ivy 13 bold'), relief=RAISED, command=lambda: atualizar_tela('6'))
b_10.place(x=118, y=104)
b_11 = Button(frame_corpo, text="-", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, command=lambda: atualizar_tela('-'))
b_11.place(x=177, y=104)
b_12 = Button(frame_corpo, text="1", width=5, height=2, bg=cor2, fg=cor1, font=('Ivy 13 bold'), relief=RAISED, command=lambda: atualizar_tela('1'))
b_12.place(x=0, y=156)  
b_13 = Button(frame_corpo, text="2", width=5, height=2, bg=cor2, fg=cor1, font=('Ivy 13 bold'), relief=RAISED, command=lambda: atualizar_tela('2'))
b_13.place(x=59, y=156) 
b_14 = Button(frame_corpo, text="3", width=5, height=2, bg=cor2, fg=cor1, font=('Ivy 13 bold'), relief=RAISED, command=lambda: atualizar_tela('3'))
b_14.place(x=118, y=156)    
b_15 = Button(frame_corpo, text="+", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, command=lambda: atualizar_tela('+'))
b_15.place(x=177, y=156) 
b_16 = Button(frame_corpo, text="0", width=11, height=2, bg=cor2, fg=cor1, font=('Ivy 13 bold'), relief=RAISED, command=lambda: atualizar_tela('0'))
b_16.place(x=0, y=208)
b_17 = Button(frame_corpo, text=".", width=5, height=2, bg=cor2, fg=cor1, font=('Ivy 13 bold'), relief=RAISED, command=lambda: atualizar_tela('.'))
b_17.place(x=118, y=208)
# b_18 button will be created after the function calcular is defined


# Variável para armazenar a expressão
expressao = ""

# Função para atualizar a tela
def atualizar_tela(valor):
	global expressao
	expressao += str(valor)
	tela.config(text=expressao)

# Função para calcular o resultado
import ast
import operator

def calcular():
	global expressao
	try:
		# Função segura para avaliar expressões matemáticas
		expr = expressao
		allowed_operators = {
			ast.Add: operator.add,
			ast.Sub: operator.sub,
			ast.Mult: operator.mul,
			ast.Div: operator.truediv,
			ast.Mod: operator.mod,
			ast.Pow: operator.pow,
			ast.USub: operator.neg,
		}
		def _eval(node):
			if isinstance(node, ast.Num):  # <number>
				return node.n
			elif isinstance(node, ast.BinOp):  # <left> <operator> <right>
				if type(node.op) in allowed_operators:
					return allowed_operators[type(node.op)](_eval(node.left), _eval(node.right))
				else:
					raise ValueError("Operador não permitido")
			elif isinstance(node, ast.UnaryOp):  # - <operand> e.g., -1
				if type(node.op) in allowed_operators:
					return allowed_operators[type(node.op)](_eval(node.operand))
				else:
					raise ValueError("Operador não permitido")
			else:
				raise ValueError("Expressão inválida")
		node = ast.parse(expr, mode='eval').body
		resultado = str(_eval(node))
		tela.config(text=resultado)
		expressao = ""
	except Exception as e:
		tela.config(text=f"Erro: {e}")
		expressao = ""

# Agora criamos o botão "=" após definir calcular
b_18 = Button(frame_corpo, text="=", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, command=calcular)
b_18.place(x=177, y=208)

# criando a tela
tela = Label(frame_tela, text="", bg=cor3, fg=cor2, font=('Ivy 18 bold'), anchor='e')
tela.place(x=0, y=0, relwidth=1, relheight=1)

# rodando a janela
janela.update_idletasks()   

janela.mainloop()
