"use client";
import type { Metadata } from "next";
import { Geist, Geist_Mono } from "next/font/google";
import "./globals.css";
import { SidebarProvider, SidebarTrigger } from "@/components/ui/sidebar";
import { AppSidebar } from "@/components/app-sidebar";
import Header from "@/components/header";
import MainSection from "@/components/mainSection";
import { Toaster } from "sonner";
import { useState } from "react";

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  const [selectedDocument, setSelectedDocument] = useState<string>("");
  return (
    <html lang="en" className={` h-full antialiased`}>
      <body>
        <SidebarProvider>
          <AppSidebar
            setSelectedDocument={setSelectedDocument}
          />
          <main className=" w-full">
            <div className="flex items-center w-full">
              <SidebarTrigger className="absolute" />
              <Header />
            </div>
            <MainSection
              selectedDocument={selectedDocument}
              setSelectedDocument={setSelectedDocument}
              
            />
            {children}
          </main>
        </SidebarProvider>
        <Toaster richColors />
      </body>
    </html>
  );
}
