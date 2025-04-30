using System;
using System.Net.Http;
using System.Threading.Tasks;

namespace DroneControl
{
    class Program
    {
        static async Task Main(string[] args)
        {
            Console.WriteLine("Say 'Initiate Drone' to start the drone thrusters.");

            while (true)
            {
                string voiceCommand = Console.ReadLine();

                if (voiceCommand.Equals("Initiate Drone", StringComparison.OrdinalIgnoreCase))
                {
                    Console.WriteLine("Initiating drone thrusters...");
                    await InitiateDroneThrusters("drone123", 0.5);
                }
                else
                {
                    Console.WriteLine("Unrecognized command. Please try again.");
                }
            }
        }

        static async Task InitiateDroneThrusters(string droneId, double powerLevel)
        {
            string endpoint = Environment.GetEnvironmentVariable("DRONE_API_ENDPOINT");
            string apiKey = Environment.GetEnvironmentVariable("DRONE_API_KEY");

            if (string.IsNullOrEmpty(endpoint))
            {
                Console.WriteLine("Drone command failed: DRONE_API_ENDPOINT not configured.");
                return;
            }

            using (HttpClient client = new HttpClient())
            {
                client.DefaultRequestHeaders.Add("Authorization", $"Bearer {apiKey}");

                var payload = new
                {
                    DroneId = droneId,
                    PowerLevel = powerLevel
                };

                try
                {
                    HttpResponseMessage response = await client.PostAsJsonAsync($"{endpoint}/initiate-thrusters", payload);
                    response.EnsureSuccessStatusCode();

                    Console.WriteLine("Drone thrusters initiated successfully.");
                }
                catch (Exception ex)
                {
                    Console.WriteLine($"Drone command failed: {ex.Message}");
                }
            }
        }
    }
}