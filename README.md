Fiz o meu projeto em python usando o Flask, com o intuito de deixa-lo funcional de maneira simples e eficiente.

Comecei criando funcoes para criar a carteira e atualiza-la apos ter iniciado o Flask. Depois disso, criei a funcao achaPrecoatual() usando a API do yahoo finance, como recomendado para guardar os valores das acoes de maneira atualizada. Usei um header ja que por algum motivo as informacoes nao estavam sendo coletadas, mas o header resolveu.

Para as paginas, criei a principal a pagina principal com os botoes de adicionar, que leva para a pagina /adicionar que coloca a acao na carteira e redireciona para a pagina principal e o botao de lucro e prejuizo que redireciona para a pagina /lucroprejuizo onde podera ver essas informacoes.

A persistencia foi feita utilizando um arquivo json, onde aparecem as novas acoes quando adicionadas e para apaga-las basta deletar o arquivo que outro sera criado, ou apagar o conteudo do arquivo.

E possivel roda-lo normalmente na IDE de escolha, colocando o endereco dado no console no browser para vizualizar o aplicativo, ou ate mesmo em uma IDE online, como o replit, onde o webview aparece direto (testei no replit usando no final app.run(host='0.0.0.0',port=8080). E necessario ter uma pasta chamada templates no mesmo diretorio do arquivo.py. 
