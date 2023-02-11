import axios from "axios";

export default {
  usuario: (usuario, callback) => {
    axios.post("http://localhost:3000/usuarios/", usuario).then((response) => {
      callback(response.data);
    });
  },
  adicionarFilme: (filme, callback) => {
    axios.post("http://localhost:3000/filmes/", filme).then((response) => {
      callback(response.data);
    });
  },

   listaFilmes: (callback) => {
    axios.get("http://localhost:3000/filmes/").then((response) => {
      callback(response.data);
    });
  },


  categoriasFilmes: (callback) => {
    axios.get("http://localhost:3000/filmes/").then((response) => {
      if (!response.data.length) {
        callback({
          Terror: 0,
          Comedia: 0,
          Ação: 0,
          Drama: 0,
          Outros: 0,
        });
        return;
      }
      let porcentagem = response.data.reduce(
        (anterior, atual) => ({
          ...anterior,
          [atual.categoria]: anterior[atual.categoria]
            ? anterior[atual.categoria] + 1
            : 1,
        }),
        {}
      );

      porcentagem = Object.entries(porcentagem).reduce(
        (anterior, atual) => ({
          ...anterior,
          [atual[0]]: (atual[1] * 100) / response.data.length,
        }),
        {}
      );

      callback(porcentagem);
    });
  },

  statusFilmes: (callback) => {
    axios.get("http://localhost:3000/filmes/").then((response) => {
      let porcentagemStatus = response.data.reduce(
        (anterior, atual) => ({
          ...anterior,
          [atual.status]: anterior[atual.status]
            ? anterior[atual.status] + 1
            : 1,
        }),
        {}
      );

      porcentagemStatus = Object.entries(porcentagemStatus).reduce(
        (anterior, atual) => ({
          ...anterior,
          [atual[0]]: (atual[1] * 100) / response.data.length,
        }),
        {}
      );

      callback(porcentagemStatus);
    });
  },

  pegarFilme: (filmeId, callback) => {
    axios.get(`http://localhost:3000/filmes/${filmeId}`).then((response) => {
      callback(response.data);
    });
  },

  salvarFilmeEditado: (filme, callback) => {
    axios
      .patch(`http://localhost:3000/filmes/${filme.id}`, filme)
      .then((response) => {
        callback(response.data);
      });
  },

  excluirFilme: (filmeId, callback) => {
    axios.delete(`http://localhost:3000/filmes/${filmeId}`).then((response) => {
      callback(response.data);
    });
  },
};
