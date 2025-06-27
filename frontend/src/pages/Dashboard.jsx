import Navbar from "../components/Navbar/Navbar";
import CarList from "../components/Cars/CarList";

const Dashboard = () => {
  return (
    <>
      <Navbar />
      <img
        className="h-[70vh] w-full object-cover"
        src="carusel-1.png"
        alt=""
      />

      <section className="mx-30 p-4">
        <CarList />
      </section>
    </>
  );
};

export default Dashboard;
