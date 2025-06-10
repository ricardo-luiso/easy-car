const CarList = () => {
  const autos = [
    {
      nombre: "Toyota Corolla",
      modelo: "2022",
      descripcion: "Compacto, confiable y eficiente.",
      imagen: "https://source.unsplash.com/featured/?toyota,corolla",
    },
    {
      nombre: "Ford Mustang",
      modelo: "2023",
      descripcion: "Deportivo clásico con potencia V8.",
      imagen: "https://source.unsplash.com/featured/?mustang,car",
    },
    {
      nombre: "Chevrolet Onix",
      modelo: "2021",
      descripcion: "Económico, ideal para la ciudad.",
      imagen: "https://source.unsplash.com/featured/?chevrolet,onix",
    },
    {
      nombre: "Honda Civic",
      modelo: "2022",
      descripcion: "Diseño moderno y buen rendimiento.",
      imagen: "https://source.unsplash.com/featured/?honda,civic",
    },
    {
      nombre: "Volkswagen Golf",
      modelo: "2023",
      descripcion: "Hatchback ágil y sofisticado.",
      imagen: "https://source.unsplash.com/featured/?volkswagen,golf",
    },
    {
      nombre: "Nissan Versa",
      modelo: "2022",
      descripcion: "Amplio, cómodo y económico.",
      imagen: "https://source.unsplash.com/featured/?nissan,versa",
    },
    {
      nombre: "Jeep Wrangler",
      modelo: "2024",
      descripcion: "4x4 ideal para aventuras off-road.",
      imagen: "https://source.unsplash.com/featured/?jeep,wrangler",
    },
    {
      nombre: "BMW Serie 3",
      modelo: "2023",
      descripcion: "Lujo, tecnología y rendimiento.",
      imagen: "https://source.unsplash.com/featured/?bmw,car",
    },
    {
      nombre: "Audi A4",
      modelo: "2023",
      descripcion: "Elegancia alemana con alto confort.",
      imagen: "https://source.unsplash.com/featured/?audi,a4",
    },
    {
      nombre: "Hyundai Elantra",
      modelo: "2022",
      descripcion: "Diseño elegante y buen consumo.",
      imagen: "https://source.unsplash.com/featured/?hyundai,elantra",
    },
  ];

  return (
    <div className="col-span-4 mx-auto px-4">
      <h1 className="text-3xl font-bold text-center my-8">Lista de Autos</h1>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {autos.map((auto, index) => (
          <div key={index} className="bg-white rounded shadow overflow-hidden">
            <img
              src={auto.imagen}
              alt={auto.nombre}
              className="w-full h-48 object-cover"
            />
            <div className="p-4">
              <h2 className="text-xl font-semibold">
                {auto.nombre} - {auto.modelo}
              </h2>
              <p className="my-2 text-gray-700">{auto.descripcion}</p>
              <button className="bg-yellow-400 hover:bg-yellow-500 text-black font-semibold py-2 px-4 rounded">
                Ver más
              </button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default CarList;
