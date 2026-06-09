"use client"
import { useState } from 'react';
import DefaultUi from './defaultUi';

const MainSection = () => {

    const [mainScreen , setMainScreen] = useState<boolean>(true)
    const [query , setQuery] = useState<string>("")

  return (
    <div className='w-full'>
      {mainScreen && <DefaultUi query = {query}  setQuery={setQuery} />}
    </div>
  )
}

export default MainSection
