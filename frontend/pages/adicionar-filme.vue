<template>
  <div>
    <forms-filmes
      :filme="filme"
      :titulo-card="tituloCard"
      :botao="botao"
      @salvarFilme="salvarFilme"
    />
  </div>
</template>

<script>
// import api from "@/api/apimock/apiMock.js";
import api from "@/api/api.js";
import formsFilmes from "@/components/forms-filmes.vue";

export default {
  components: {
    formsFilmes,
  },
  data: () => {
    return { 
      categorias: [],
      filmes: [],
      tituloCard: "Cadastre um novo filme",
      botao: "Adicionar",
      // objeto que envio para o forms-filme
      filme:{
        id: 0,
        status: "Pendente",
        categoria: "",
        titulo: "",
        descricao: "",
        imagem: "",
      }
    };
  },

  created() {
    this.listaFilmes();
  },

  methods: {
    salvarFilme(novoFilme) {
      api.adicionarFilme(novoFilme).then(this.listaFilmes())
      this.$router.push("/exibir-filmes");
    },

    listaFilmes() {
      api.listaFilmes().then(response => {
          this.filmes = response.filmes;
      });
    }
  },
};
</script>
