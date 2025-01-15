import sqlite3

def create_db():
    conn = sqlite3.connect('data/database.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS contexto (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, conteudo TEXT)')
    cursor.execute('CREATE TABLE IF NOT EXISTS historico (id INTEGER PRIMARY KEY AUTOINCREMENT, tipo TEXT, legenda TEXT, desc_img TEXT, roteiro_video TEXT)')
    conn.commit()
    conn.close()

def insert_contexto(nome, conteudo):
    conn = sqlite3.connect('data/database.db')
    cursor = conn.cursor()
    insert_query = f"INSERT INTO contexto (nome, conteudo) VALUES ('{nome}', '{conteudo}')"
    cursor.execute(insert_query)
    conn.commit()
    conn.close()

create_db()
produtos_ctx = f"""
Os produtos que vendo atualmente são:
- AIA: o mínimo para prosperar. AIA é uma sigla que significa Automação e Inteligência Artificial, o produto se trata de um curso que ensina o básico de forma robusta sobre automação e inteligência artificial e engenharia de prompt para aqueles que sabem nada ou muito pouco sobre o tema e sentem que precisam aprender mais e não sabem por onde começar.
- BotCollie: é um software de automação de tarefas no desktop. Ele é bem intuitivo e possui uma curva de aprendizado bem pequena, não precisa de nenhum conhecimento de programação para conseguir criar e editar as automações nele. Ele automatiza cliques no teclado e no mouse, ou seja, toda e qualquer atividade repetitiva ele consegue automatizar. Por enquanto apenas a versão para windows está disponível.
"""
estrategia_ctx = f"""
A objetivo principal no uso da redes sociais é obter mais leads, ou seja, alcançar as pessoas interessadas nos produtos que vendo e fazê-las entrar na minha página de vendas e assistir a minha aula gratuita onde faço uma oferta especial.
A estratégia que vamos seguir tem como base a Pirâmide de Chet Holmes. E a nossa atuação nas redes sociais será para ir atrás do segundo grupo mais ao topo da pirâmide, a saber são os 7% que estão interessados em ouvir e abertos a ideia de comprar. Esse grupo de pessoas que vamos atrás não está necessariamente em busca ativa, mas está aberto à ideia de comprar se surgir uma boa oportunidade ou solução. Para fazer as pessoas entrarem na página de vendas vou utilizar anúncios pagos no facebook e Instagram. A missão é preencher o perfil do Instagram com conteúdo bom e que seja chamativo e realmente interessante para meu público alvo sem ser apelativo. Portanto vou precisar de posts e reels pois meu perfil ainda está vazio.
Para os conteúdos pretendo utilizar a seguinte estrutura de roteiro:
1. Mostrar que eu entendo do que falo, explicar algum conceito do tema que domino.
2. Mostrar que eu resolvo os problemas que me proponho a resolver.
3. Mostrar melhor quem sou, expor algum aspecto da minha vida pessoal com a finalidade de criar proximidade com as pessoas que chegam
Essa estrutura deverá ser cíclica, ou seja, um conteúdo de cada por postagem sem repetir o anterior.
"""
publico_alvo_ctx = f"""
O público alvo que se deseja alcançar são os seguintes:
- Funcionários CLT de qualquer área no nível de analista para cima
- Líderes executivos
- Profissionais freelancers
- Qualquer profissional do mercado digital, exemplo: designers, social media, copywriters etc.
"""
planejamento_ctx = f"""
O planejamento não será agressivo nesse primeiro momento, por questões práticas, não consigo postar com frequência e também porque o foco agora é vender via anúncios pagos como explicado na estratégia. Portanto vamos fazer um post por semana no Instagram. O tipo de publicação você decide, lembrando da estratégia a ser usada no Instagram.
"""
personalidade_ctx = f"""
Felipe Gonçalves, nascido em 20/12/1992, casado com 2 filhos e formado em engenharia de controle e automação e trabalhou como desenvolvedor em empresas pequenas, médias e grandes.
Segue resultado de teste de personalidade feita pelo dono da conta e especialista quem criou os produtos e as estratégias explicadas:
INTJ-A ("Arquiteto")
Energia: 64% introvertido
Mente: 63% realista
Natureza: 64% analítico
Abordagem: 78% planejador
Identidade: 99% assertivo
"""
insert_contexto('Produtos', produtos_ctx)
insert_contexto('Estratégia', estrategia_ctx)
insert_contexto('Público Alvo', publico_alvo_ctx)
insert_contexto('Planejamento', planejamento_ctx)
insert_contexto('Personalidade do cliente', personalidade_ctx)
