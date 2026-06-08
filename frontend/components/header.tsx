import React from 'react' ; 
import LlmListe from './llmListe';


const Header = () => {
  return (
    <div className='p-3 px-12 items-center  flex w-full  justify-between   border-b border-b-stone-300'>
    <h2 className="font-semibold text-lg">Document Assistant</h2>
      <LlmListe />
    </div>
  )
}

export default Header
