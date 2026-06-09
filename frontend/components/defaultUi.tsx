import React from "react";
import { FileText, Send } from "lucide-react";
import { Input } from "./ui/input";

const DefaultUi = ({
  query,
  setQuery,
}: {
  query: string;
  setQuery: React.Dispatch<React.SetStateAction<string>>;
}) => {
  return (
    <div className="flex items-center justify-center w-full min-h-[80vh] px-4">
      <div className="w-full max-w-3xl">
        <div className="text-center mb-8">
          

          <h1 className="text-4xl font-bold tracking-tight text-primary/90">
            Ask anything about your documents
          </h1>

          <p className="mt-3 text-base text-muted-foreground">
            Upload a PDF or TXT file and start chatting with your content.
          </p>
        </div>

        <div className="relative">
          <Input
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            placeholder="Ask anything about your documents..."
            className="
              h-14
              rounded-md
              pr-14
              text-base
              shadow-sm
              border-border/60
              focus-visible:ring-1
              focus-visible:border-ring/20
            "
          />

          <button
            type="button"
            className="
              absolute
              right-2
              top-1/2
              -translate-y-1/2
              flex
              h-10
              w-10
              items-center
              justify-center
              rounded-md
              bg-secondary
              text-white
              transition
              hover:bg-ring/20
               hover:cursor-pointer
            "
          >
            <Send className="h-4 w-4 text-primary/60 hover:text-primary/70 hover:cursor-pointer" />
          </button>
        </div>
      </div>
    </div>
  );
};

export default DefaultUi;
