<template>
  <div>
    <listar-filmes
      :filmes="filmes"
      @selecionarFilmeEdicao="selecionarFilmeEdicao"
      @excluirFilme="excluirFilme"
      @adicionarNovoFilme="adicionarNovoFilme"
    />
  </div>
</template>

<script>
// import api from "@/api/apimock/apiMock.js";
import api from "@/api/api.js";
import listarFilmes from "@/components/listar-filmes.vue";

export default {
  components: {
    listarFilmes,
  },

  data: () => {
    return {
      categorias: [],
      filmes: [],
      categoria: "",
      titulo: "",
      descricao: "",
      id: 0,
      botao: "",
      tituloCard: "",
      status: ""
    };
  },
  created() {
    this.listaFilmes();
  },

  methods: {
    listaFilmes() {
      api.listaFilmes().then(response => {
          this.filmes = response.filmes;
      });
    },

    selecionarFilmeEdicao(filmeId) {
      this.$router.push(`/editar-filme/${filmeId}`);
    },

    adicionarNovoFilme(novoFilme) {
      this.$router.push("/adicionar-filme", novoFilme);
    },

    excluirFilme(filmeId) {
      api.excluirFilme(filmeId).then(this.listaFilmes())
      this.$router.push("/exibir-filmes");
    },
  },
};
</script>
