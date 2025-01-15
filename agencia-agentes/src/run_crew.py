from src.handle_db import get_contexto

class AgenciaMarketing:
    def __init__(self):
        self.contexto = get_contexto()
        self.contexto_text = self.build_contexto_text()
        #self.historico = get_historico()

    def build_contexto_text(self):
        ctx_text = ""
        for ctx in self.contexto:
            nome_ctx = ctx[1]
            conteudo_ctx = ctx[2]
            ctx_text += f"{nome_ctx}: {conteudo_ctx}\n"
        print(ctx_text)
        return ctx_text
    
    def agente_estratégico(self):
        pass

    def agente_de_criação(self):
        pass

    def agente_de_revisão(self):
        pass

AgenciaMarketing()
