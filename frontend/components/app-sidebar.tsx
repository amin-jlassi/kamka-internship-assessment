"use client";

import {
  Sidebar,
  SidebarContent,
  SidebarFooter,
  SidebarGroup,
  SidebarHeader,
  SidebarGroupLabel,
} from "@/components/ui/sidebar";

import { Button } from "./ui/button";
import { Spinner } from "./ui/spinner";
import { useEffect, useRef, useState } from "react";
import { error } from "console";

export function AppSidebar() {
  const [loading, setLoading] = useState(false);
  const [documents, setDocuments] = useState<string[]>([]);

  const fetchDocuments = async () => {
    try {
      const response = await fetch(
        `${process.env.NEXT_PUBLIC_BACKEND_URL}/documents`,
      );

      if (!response.ok) {
        throw new Error("Failed to fetch documents");
      }

      const data = await response.json();
      setDocuments(data.documents);
    } catch (error) {
      console.error("Fetch documents error:", error);
      throw error;
    }
  };
  useEffect(()=>{
    fetchDocuments()
  },[])
  const fileInputRef = useRef<HTMLInputElement | null>(null);

  async function uploadDocument(file: File) {
    try {
      const formData = new FormData();
      formData.append("file", file);

      const response = await fetch(
        `${process.env.NEXT_PUBLIC_BACKEND_URL}/upload`,
        {
          method: "POST",
          body: formData,
        },
      );

      if (!response.ok) {
        const error = await response.text()
        throw new Error(error || "upload failed");
      }

      return await response.json();
    } catch (error) {
      console.error("Upload error:", error);
      throw error;
    }
  }

  const handleFileChange = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) return;

    setLoading(true);

    try {
      const data = await uploadDocument(file);

      if (data?.filename) {
        setDocuments((prev) => [...prev, data.filename]);
      }
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <Sidebar>
      <SidebarHeader />

      <SidebarContent>
        <SidebarGroup>
          <SidebarGroupLabel className="text-md">Documents</SidebarGroupLabel>

          <div className="px-2 text-sm text-muted-foreground">
            {documents.length === 0 ? (
              <p className="text-xs px-1">No documents uploaded yet.</p>
            ) : (
              documents.map((document, i) => <div key={i}>• {document}</div>)
            )}
          </div>
        </SidebarGroup>
      </SidebarContent>

      <SidebarFooter>
        <div className="flex flex-col gap-2 px-2">
          <input
            ref={fileInputRef}
            type="file"
            accept=".pdf,.txt"
            className="hidden"
            onChange={handleFileChange}
          />

          <Button
            className="w-full"
            disabled={loading}
            onClick={() => fileInputRef.current?.click()}
          >
            {loading ? (
              <span className="flex items-center gap-2">
                <Spinner />
                Uploading...
              </span>
            ) : (
              "Upload document"
            )}
          </Button>
        </div>
      </SidebarFooter>
    </Sidebar>
  );
}
