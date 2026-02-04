import "./globals.css";

export const metadata = {
  title: "Geographer Fun Lab",
  description:
    "Spin up geography challenges and playful cartography facts powered by a Python microservice."
};

export default function RootLayout({
  children
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className="layout-body">{children}</body>
    </html>
  );
}
