import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";

const CarList = () => {
  const navigate = useNavigate();
  const [busqueda, setBusqueda] = useState("");
  const [autos, setAutos] = useState([]);
  const autosFiltrados = autos.filter((auto) =>
    `${auto.nombre} ${auto.color_id} ${auto.marca_id} ${auto.modelo_id} ${auto.estado_id}`
      .toLowerCase()
      .includes(busqueda)
  );

  const getAutos = async () => {
    const token = localStorage.getItem("token");
    const response = await fetch("http://localhost:8000/autos/", {
      method: "GET",
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });
    const data = await response.json();
    setAutos(data);
  };

  useEffect(() => {
    getAutos();
  }, []);

  return (
    <div className="col-span-4 mx-auto max-w-7xl px-4">
      <h1 className="text-4xl font-bold text-center my-8 text-gray-800">
        Lista de Autos
      </h1>

      {/* Nota informativa */}
      <div className="mb-4 text-center text-gray-600 text-sm">
        Podés buscar por <strong>nombre</strong>, <strong>marca</strong>,{" "}
        <strong>modelo</strong>, <strong>color</strong> o{" "}
        <strong>estado</strong> (por ejemplo: "toyota", "rojo", "usado",
        "hilux")
      </div>

      {/* Barra de búsqueda estilizada */}
      <div className="mb-8">
        <input
          type="text"
          placeholder="🔍 Buscar autos..."
          className="w-full p-3 rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-yellow-400 shadow-sm transition"
          value={busqueda}
          onChange={(e) => setBusqueda(e.target.value.toLowerCase())}
        />
      </div>

      {/* Condicional para mostrar autos o mensaje de vacío */}
      {autosFiltrados.length === 0 ? (
        <div className="text-center text-gray-500 text-lg mt-32 mb-20">
          🚫 No se encontraron autos que coincidan con la búsqueda.
        </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          {autosFiltrados.map((auto, index) => (
            <div
              key={index}
              className="bg-white rounded-xl shadow-md overflow-hidden flex flex-col justify-between transition transform hover:scale-[1.01]"
            >
              <img
                src={`http://localhost:8000${auto.imagen}`}
                alt={auto.nombre}
                className="w-full h-60 object-contain bg-gray-100"
              />

              <div className="p-4 flex flex-col justify-between h-full">
                <div>
                  <h3 className="text-xl font-semibold mb-2 text-gray-800">
                    {auto.nombre}
                  </h3>
                  <p className="text-sm text-gray-600">
                    <span className="font-semibold">Marca:</span>{" "}
                    <span className="capitalize">{auto.marca_id}</span>
                  </p>
                  <p className="text-sm text-gray-600">
                    <span className="font-semibold">Modelo:</span>{" "}
                    <span className="capitalize">{auto.modelo_id}</span>
                  </p>
                  <p className="text-sm text-gray-600">
                    <span className="font-semibold">Estado:</span>{" "}
                    <span className="capitalize">{auto.estado_id}</span>
                  </p>
                  <p className="text-sm text-gray-600 mb-4">
                    <span className="font-semibold">Color:</span>{" "}
                    <span className="capitalize">{auto.color_id}</span>
                  </p>
                </div>

                <button
                  onClick={() => navigate(`/perfil-auto/${auto.id}`)}
                  className="hover:cursor-pointer mt-auto bg-yellow-400 hover:bg-yellow-500 text-black font-semibold py-2 px-4 rounded w-full transition"
                >
                  Ver más
                </button>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default CarList;
