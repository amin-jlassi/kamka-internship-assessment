"use client";
import { useEffect, useState } from "react";
import DefaultUi from "./defaultUi";
import { Send } from "lucide-react";
import { Input } from "./ui/input";
import { Spinner } from "./ui/spinner";

const MainSection = () => {
  const [mainScreen, setMainScreen] = useState<boolean>(true);
  const [query, setQuery] = useState<string>("");
  const [answer_response, setAnswer_response] = useState<
    { query: string; answer: string }[]
  >([]);
  const [laoding, setLoading] = useState<boolean>(true);

  const getAnswer = async (query: string) => {
    try {
      setAnswer_response((prev) => [...prev, { query: query, answer: "" }]);
      setLoading(true);
      const request = await fetch(
        `${process.env.NEXT_PUBLIC_BACKEND_URL}/chat`,
        {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ query: query, filename: null }),
        },
      );
      if (request.ok) {
        const response = await request.json();
        console.log(response);
        setLoading(false);
        setAnswer_response((prev) =>
          prev.map((item, index) =>
            index === prev.length - 1
              ? { ...item, answer: response.answer }
              : item,
          ),
        );
      } else {
        setLoading(false);
      }
    } catch (err) {
      setLoading(false);
      console.log(err);
    }

    setQuery("");
  };

  useEffect(() => {
    if (mainScreen == false) {
      getAnswer(query);
    }
  }, [mainScreen]);

  return (
    <div className="w-full">
      {mainScreen && (
        <DefaultUi
          setMainScreen={setMainScreen}
          query={query}
          setQuery={setQuery}
        />
      )}

      {!mainScreen && (
        <div className="w-[90%] m-auto">
          <div className="w-full mt-12">
            {answer_response.map((item, index) => (
              <div className="w-full" key={index}>
                {/* user query */}
                <div className="flex justify-end">
                  <div className="bg-secondary px-4 py-2 rounded-md w-fit mt-4 max-w-[60%] text-right">
                    {item.query}
                  </div>
                </div>
                {/* agent response */}
                <div className="flex justify-start">
                  {laoding ? (
                    <Spinner />
                  ) : (
                    <div className=" px-4 py-6 rounded-md w-fit max-w-[full] text-left">
                      {item.answer}
                    </div>
                  )}
                </div>
              </div>
            ))}
          </div>

          <div className="fixed bottom-5 mr-45 right-0 w-[70%]">
            <div>
              <Input
                value={query}
                onChange={(e) => setQuery(e.target.value)}
                placeholder="Ask anything about your documents..."
                className="h-14 rounded-md pr-14 text-base shadow-sm border-border/60 focus-visible:ring-1 focus-visible:border-ring/20"
              />

              <button
                disabled={query == ""}
                onClick={() => getAnswer(query)}
                type="button"
                className="absolute disabled:opacity-50 disabled:cursor-not-allowed right-2 top-1/2 -translate-y-1/2 flex h-10 w-10 items-center justify-center rounded-md bg-secondary text-white transition hover:bg-ring/20 hover:cursor-pointer"
              >
                <Send className="h-4 w-4 text-primary/60 hover:text-primary/70 hover:cursor-pointer" />
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default MainSection;
