# Lista de Supermercado

Aplicação web leve para criar e acompanhar uma lista de compras, organizar produtos por categoria, estimar valores e manter uma base local de preços de referência.

O projeto foi pensado para uso direto no navegador e pode ser publicado como site estático, por exemplo no GitHub Pages.

## Principais recursos

- Lista de compras organizada por categorias.
- Marcação de itens comprados e pendentes.
- Totais de **Total**, **No carrinho** e **Faltando**.
- Quantidades por unidade, fração, peso, volume e embalagem.
- Sugestão de preço conforme produto e quantidade.
- Consulta a `precos.csv` para atualizar a base de preços.
- Cache local da última base de preços baixada.
- Edição manual dos preços de referência.
- Inclusão de produtos personalizados.
- Edição e exclusão dos itens da lista.
- Impressão da lista.
- Cópia dos itens pendentes para compartilhamento.
- Exportação e importação da lista em JSON.
- Dados da lista salvos no próprio navegador com `localStorage`.

## Arquivos

Estrutura básica recomendada:

```text
/
├── index.html
├── precos.csv
└── README.md
```

O `index.html` procura a base de preços usando o caminho relativo:

```javascript
const MARKET_CSV_URL = './precos.csv';
```

Por isso, mantenha `precos.csv` na mesma pasta do `index.html`, salvo se você também alterar esse endereço no código.

## Executar

### Publicado na internet

Publique `index.html` e `precos.csv` juntos em um servidor HTTPS ou serviço de hospedagem estática. Abra então o endereço publicado no navegador.

### Desenvolvimento local

É recomendável servir a pasta por um servidor HTTP local em vez de abrir apenas o arquivo HTML por `file://`, pois o aplicativo usa `fetch()` para carregar `precos.csv`.

Um exemplo, caso já tenha Python instalado:

```bash
python -m http.server 8000
```

Depois acesse `http://localhost:8000` no navegador.

## Atualização dos preços

O botão **🔄 Atualizar preços** solicita novamente `precos.csv` e guarda no navegador uma cópia da base recebida. Se houver uma base local já salva, ela pode continuar sendo utilizada quando uma nova atualização não estiver disponível.

> `precos.csv` é a fonte publicada para o aplicativo. O botão não pesquisa preços de mercado por conta própria. Para atualizar valores de mercado, o próprio arquivo CSV precisa ser atualizado por uma fonte externa ou processo de atualização.

## Como usar

1. Escolha a categoria.
2. Escolha o produto.
3. Selecione a quantidade, peso, volume ou embalagem.
4. Use a sugestão de preço ou informe outro valor.
5. Pressione **+** para inserir o produto.
6. Marque o item quando colocá-lo no carrinho.
7. Toque ou clique em um item para editá-lo.

A página salva automaticamente a lista no armazenamento local do navegador.

## Instalar no navegador como aplicativo

A instalação depende do navegador e do sistema operacional. Para a experiência de PWA instalável, navegadores normalmente utilizam um **Web App Manifest** e critérios próprios de instalação. O `index.html` atual não contém referência a um manifesto, portanto alguns navegadores podem oferecer apenas a instalação do site/atalho, e outros podem não apresentá-lo como PWA instalável.

### Microsoft Edge no Windows/macOS

O Edge permite instalar inclusive um site como aplicativo:

1. Abra o endereço publicado no Microsoft Edge.
2. Abra **Configurações e mais (...)**.
3. Entre em **Mais ferramentas > Aplicativos**.
4. Escolha **Instalar este site como um aplicativo**.
5. Confirme a instalação.

Os aplicativos instalados podem ser gerenciados na página `edge://apps` do próprio Edge.

### Google Chrome no computador

Para sites que atendem aos critérios de instalação de PWA, Chrome e Edge podem exibir um ícone de instalação na barra de endereço.

1. Abra o aplicativo no Chrome.
2. Se o navegador mostrar o ícone/opção de instalação, selecione **Instalar**.
3. Confirme.

Se a opção não aparecer, o site pode não estar atendendo aos critérios de PWA do Chrome. Veja a seção **Transformar em PWA completo** abaixo.

### Android com Google Chrome

1. Abra o endereço do aplicativo no Chrome.
2. Toque no menu **⋮**.
3. Escolha a opção de **Instalar** ou de criar/adicionar o atalho oferecida pelo navegador.
4. Siga as instruções exibidas na tela.

### iPhone com Safari

A Apple permite transformar um site em web app pela Tela de Início:

1. Abra o endereço no Safari.
2. Toque em **Compartilhar**.
3. Escolha **Adicionar à Tela de Início**.
4. Quando disponível, ative **Abrir como App da Web**.
5. Toque em **Adicionar**.

O ícone será colocado na Tela de Início.

## Transformar em PWA completo

Para tornar o projeto explicitamente instalável como PWA nos navegadores compatíveis, a próxima versão deve acrescentar pelo menos a configuração apropriada de um **Web App Manifest**. Uma implementação PWA também pode usar um Service Worker para definir o comportamento de cache/offline.

Estrutura futura sugerida:

```text
/
├── index.html
├── precos.csv
├── manifest.webmanifest
├── service-worker.js
├── icons/
│   ├── icon-192.png
│   └── icon-512.png
└── README.md
```

> A presença desses arquivos, sozinha, não substitui a configuração correta. Os critérios de instalação variam conforme navegador e plataforma.

## Dados e privacidade

A lista de compras, produtos personalizados e alterações locais de preços são armazenados pelo navegador no dispositivo. O aplicativo também oferece exportação em JSON para criar uma cópia dos dados.

Ao limpar os dados do site/navegador, informações mantidas apenas no armazenamento local podem ser removidas. Faça uma exportação JSON quando quiser conservar um backup independente.

## Backup e restauração

### Exportar

Use **Exportar .json** para baixar a lista e os preços de referência alterados.

### Importar

Use **Importar .json** e selecione um arquivo anteriormente exportado pelo aplicativo.

## Compatibilidade

O projeto utiliza recursos web modernos, incluindo JavaScript, `localStorage`, `fetch()`, Clipboard API quando disponível e impressão pelo navegador.

Para melhor funcionamento, mantenha o navegador atualizado.

## Observação sobre preços

Os valores apresentados devem ser tratados como referências. Preços efetivos podem variar conforme produto, marca, estabelecimento, região, promoção e data da compra.

## Licença

Nenhuma licença foi definida neste README. Se o repositório for disponibilizado publicamente para reutilização por terceiros, adicione uma licença adequada ao projeto.
