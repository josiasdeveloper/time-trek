from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Historical Facts API", description="Mock API that returns historical facts from June 2004")

# JSON data hardcoded
historical_facts_data = {
   "date": "2004-06",
   "timestamp": "2025-04-06T12:35:25.030214Z",
   "total_facts": 7,
   "historical_facts": [
      {
         "title": "Co-conspirador do atentado de Oklahoma City, Terry Nichols, é condenado a 161 penas de prisão perpétua consecutivas sem possibilidade de liberdade condicional, quebrando um recorde mundial do Guinness.",
         "content": "Em 4 de junho de 2004, Terry Nichols foi condenado a 161 penas de prisão perpétua consecutivas sem possibilidade de liberdade condicional pelo seu papel no atentado de Oklahoma City em 1995. Este ataque, que destruiu o Edifício Federal Alfred P. Murrah, resultou na morte de 168 pessoas e foi o ato de terrorismo doméstico mais mortal na história dos Estados Unidos até então. A sentença de Nichols reflete a gravidade do crime e a busca por justiça para as vítimas e suas famílias. O atentado teve um impacto profundo na segurança nacional e nas políticas antiterrorismo nos EUA, levando a um aumento na vigilância e na legislação contra o terrorismo doméstico.",
         "attachments": None
      },
      {
         "title": "Noël Mamère, prefeito de Bègles, celebra casamento entre dois homens pela primeira vez na França.",
         "content": "Em 5 de junho de 2004, Noël Mamère, então prefeito de Bègles, uma cidade próxima a Bordeaux, realizou o primeiro casamento entre pessoas do mesmo sexo na França, unindo Stéphane Chapin e Bertrand Charpentier. Este ato ocorreu nove anos antes da legalização oficial do casamento homoafetivo no país, que aconteceu em 2013 com a aprovação da lei conhecida como 'Mariage pour tous'. A cerimônia de 2004 foi um marco na luta pelos direitos LGBTQ+ na França, gerando debates acalorados e enfrentando oposição significativa. Mamère enfrentou sanções, incluindo uma suspensão de um mês de suas funções como prefeito. Apesar das controvérsias, este evento destacou a necessidade de igualdade de direitos e contribuiu para a evolução das políticas de inclusão e reconhecimento dos direitos das pessoas LGBTQ+ na França.",
         "attachments": [
            "https://france3-regions.francetvinfo.fr/nouvelle-aquitaine/gironde/bordeaux/mariage-pour-tous-en-2004-noel-mamere-a-celebre-le-premier-mariage-homosexuel-9-ans-avant-la-loi-2759230.html",
            "https://www.bfmtv.com/societe/pas-tant-de-monde-contre-nous-noel-mamere-revient-sur-le-mariage-gay-illegal-celebre-il-y-a-20-ans_AN-202406051079.html"
         ]
      },
      {
         "title": "O primeiro Trânsito de Vênus em mais de um século ocorre, o anterior sendo em 1882.",
         "content": "Em 8 de junho de 2004, ocorreu um evento astronômico raro conhecido como Trânsito de Vênus, no qual o planeta Vênus passou diretamente entre a Terra e o Sol, aparecendo como um pequeno disco escuro movendo-se através do disco solar. Este foi o primeiro trânsito desde 1882, tornando-se um evento significativo para astrônomos e entusiastas. Trânsitos de Vênus ocorrem em pares separados por oito anos, com intervalos de mais de um século entre esses pares. O próximo trânsito após 2004 ocorreu em 2012, e o seguinte será em 2117. Historicamente, esses trânsitos foram cruciais para os astrônomos determinarem a distância entre a Terra e o Sol, conhecida como Unidade Astronômica. No Brasil, o Grupo de Estudos de Astronomia (GEA) realizou uma observação detalhada do trânsito de 2004 em Florianópolis, destacando a importância histórica e científica do evento.",
         "attachments": [
            "https://www.gea.org.br/memoria/historia-do-grupo/a-observacao-do-transito-de-venus-em-08-06-2004/"
         ]
      },
      {
         "title": "Cassini-Huygens faz seu sobrevoo mais próximo da lua de Saturno, Febe.",
         "content": "Em 11 de junho de 2004, a sonda espacial Cassini-Huygens realizou um sobrevoo próximo da lua Febe de Saturno, aproximando-se a uma distância de 2.068 quilômetros. Este foi o primeiro encontro próximo da missão Cassini-Huygens com uma das luas de Saturno, fornecendo imagens e dados detalhados sobre Febe. Os cientistas estavam particularmente interessados em Febe devido à sua órbita retrógrada e composição, sugerindo que poderia ser um objeto capturado do Cinturão de Kuiper. O sobrevoo permitiu a criação de mapas globais da lua e a determinação de sua composição, massa e densidade, contribuindo significativamente para a compreensão da formação e evolução do sistema de Saturno.",
         "attachments": [
            "https://www.emol.com/noticias/internacional/2004/06/12/150151/sonda-espacial-realiza-su-primer-contacto-con-luna-de-saturno.html"
         ]
      },
      {
         "title": "SpaceShipOne torna-se a primeira espaçonave financiada privadamente a alcançar o espaço",
         "content": "Em 21 de junho de 2004, a SpaceShipOne realizou o primeiro voo espacial humano financiado exclusivamente por recursos privados. Desenvolvida pela empresa Scaled Composites, sob a liderança do designer aeroespacial Burt Rutan e com financiamento do cofundador da Microsoft, Paul Allen, a SpaceShipOne atingiu uma altitude de 100 km, marcando a fronteira do espaço. Este feito não apenas demonstrou a viabilidade de voos espaciais privados, mas também abriu caminho para o desenvolvimento do turismo espacial comercial. Posteriormente, em outubro do mesmo ano, a SpaceShipOne conquistou o Prêmio Ansari X de US$ 10 milhões ao realizar dois voos espaciais tripulados em um período de duas semanas.",
         "attachments": [
            "https://pt.wikipedia.org/wiki/SpaceShipOne"
         ]
      },
      {
         "title": "Em Nova York, pena de morte é declarada inconstitucional",
         "content": "Em junho de 2004, o Tribunal de Apelações do Estado de Nova York declarou inconstitucional a lei estadual que permitia a aplicação da pena de morte. A decisão baseou-se na interpretação de que a lei violava a constituição estadual, especificamente no que diz respeito às instruções dadas aos jurados durante o processo de condenação. Esta decisão refletiu uma tendência crescente nos Estados Unidos de reavaliar a aplicação da pena capital, considerando questões de direitos humanos e possíveis erros judiciais. Como resultado, Nova York suspendeu a aplicação da pena de morte, alinhando-se a outros estados que também reconsideravam suas políticas sobre o tema.",
         "attachments": None
      },
      {
         "title": "Guerra do Iraque: Poder soberano é transferido ao governo interino do Iraque pela Autoridade Provisória da Coalizão, encerrando o domínio liderado pelos EUA sobre a nação.",
         "content": "Em 28 de junho de 2004, a Autoridade Provisória da Coalizão (APC), liderada pelos Estados Unidos, transferiu antecipadamente a soberania ao governo interino iraquiano, encerrando oficialmente a ocupação que havia começado em abril de 2003. Originalmente prevista para 30 de junho, a transferência foi adiantada para evitar possíveis ataques insurgentes durante a cerimônia. O administrador civil dos EUA no Iraque, Paul Bremer, entregou documentos ao primeiro-ministro interino Iyad Allawi, marcando o início de uma nova fase para o país. Apesar da transferência de poder, uma força multinacional de mais de 150 mil soldados, sob comando dos EUA, permaneceu no Iraque para garantir a segurança. A decisão de antecipar a transferência foi anunciada pelo ministro das Relações Exteriores do Iraque, Hoshiar Zebari, durante a cúpula da OTAN em Istambul, como uma medida para evitar novos atentados terroristas. O governo alemão saudou a antecipação, considerando-a um passo importante para o retorno do Iraque ao círculo das nações independentes. No entanto, desafios significativos permaneceram, incluindo a escalada da violência e a necessidade de estabelecer uma democracia estável em um país sem histórico democrático.",
         "attachments": [
            "https://www.dw.com/pt-br/berlim-sa%C3%BAda-soberania-antecipada-para-o-iraque/a-1248812",
            "https://www.estadao.com.br/internacional/eua-antecipam-entrega-de-soberania-do-iraque/"
         ]
      }
   ],
   "metadata": {
      "source": "API Ninjas",
      "enhanced_by": "GPT-3.5",
      "batch_size": 2
   }
}

@app.get("/")
async def root():
    """
    Endpoint raiz que exibe uma mensagem de boas-vindas e instruções básicas.
    """
    return {
        "message": "Bem-vindo à API de Fatos Históricos",
        "endpoints": {
            "/facts": "Retorna todos os fatos históricos de junho de 2004",
            "/facts/{fact_id}": "Retorna um fato histórico específico pelo seu índice (0-6)"
        }
    }

@app.get("/api/historical-facts")
async def get_all_facts(day: int, month: int, year: int):
    """
    Retorna todos os fatos históricos cadastrados no sistema.
    """
    return historical_facts_data

@app.get("/facts/{fact_id}")
async def get_fact_by_id(fact_id: int, response: Response):
    """
    Retorna um fato histórico específico com base no ID fornecido.
    
    Args:
        fact_id: O índice do fato histórico (começando em 0)
        
    Returns:
        O fato histórico específico ou uma mensagem de erro se o ID for inválido
    """
    if 0 <= fact_id < len(historical_facts_data["historical_facts"]):
        return historical_facts_data["historical_facts"][fact_id]
    
    response.status_code = 404
    return {"error": "Fato histórico não encontrado"}

@app.get("/metadata")
async def get_metadata():
    """
    Retorna apenas os metadados da API.
    """
    return historical_facts_data["metadata"]

@app.get("/health")
async def health_check():
    """
    Endpoint simples para verificação de saúde da API.
    """
    return {"status": "ok", "timestamp": historical_facts_data["timestamp"]}


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)