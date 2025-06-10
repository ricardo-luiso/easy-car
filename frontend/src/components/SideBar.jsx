const SideBar = () => {
  return (
    <>
      <div className="col-span-1 sidebar mx-auto w-full">
        <h2 className="text-xl text-center font-bold mb-4 text-white bg-cyan-500 p-2 rounded-md">
          Filtros
        </h2>

        {/* Filtro por Color */}
        <div className="mb-6 bg-gray-200 p-2 rounded-md border border-gray-300">
          <h3 className="font-semibold mb-2">Color</h3>
          <div className="space-y-1">
            <label className="flex items-center">
              <input type="checkbox" className="mr-2" /> Rojo
            </label>
            <label className="flex items-center">
              <input type="checkbox" className="mr-2" /> Azul
            </label>
            <label className="flex items-center">
              <input type="checkbox" className="mr-2" /> Negro
            </label>
          </div>
        </div>

        {/* Filtro por Estado */}
        <div className="mb-6 bg-gray-200 p-2 rounded-md border border-gray-300">
          <h3 className="font-semibold mb-2">Estado</h3>
          <div className="space-y-1">
            <label className="flex items-center">
              <input type="checkbox" className="mr-2" /> Nuevo
            </label>
            <label className="flex items-center">
              <input type="checkbox" className="mr-2" /> Usado
            </label>
          </div>
        </div>

        {/* Filtro por Marca */}
        <div className="mb-6 bg-gray-200 p-2 rounded-md border border-gray-300">
          <h3 className="font-semibold mb-2">Marca</h3>
          <div className="space-y-1">
            <label className="flex items-center">
              <input type="checkbox" className="mr-2" /> Toyota
            </label>
            <label className="flex items-center">
              <input type="checkbox" className="mr-2" /> Ford
            </label>
            <label className="flex items-center">
              <input type="checkbox" className="mr-2" /> Chevrolet
            </label>
          </div>
        </div>

        {/* Filtro por Modelo */}
        <div className="mb-6 bg-gray-200 p-2 rounded-md border border-gray-300">
          <h3 className="font-semibold mb-2">Modelo</h3>
          <div className="space-y-1">
            <label className="flex items-center">
              <input type="checkbox" className="mr-2" /> 2022
            </label>
            <label className="flex items-center">
              <input type="checkbox" className="mr-2" /> 2023
            </label>
            <label className="flex items-center">
              <input type="checkbox" className="mr-2" /> 2024
            </label>
          </div>
        </div>
      </div>
    </>
  );
};

export default SideBar;
