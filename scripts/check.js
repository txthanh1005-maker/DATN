const fs = require('fs');
const https = require('https');

const dois = [
    '10.1109/access.2024.3382940',
    '10.1109/tii.2024.3478274',
    '10.1007/s10589-022-00433-4',
    '10.1109/epee59859.2023.10351909',
    '10.3389/fenrg.2024.1438961',
    '10.1155/2020/4215906',
    '10.1109/TSG.2019.2947935',
    '10.1109/cac59555.2023.10451685',
    '10.1109/TPWRS.2021.3060595',
    '10.1109/TSG.2019.2933458',
    '10.1109/tsg.2020.3010570',
    '10.1109/access.2020.2968586',
    '10.1109/tcst.2022.3208456',
    '10.1109/tase.2024.3485922',
    '10.1016/j.ijepes.2021.107126',
    '10.1016/j.ijepes.2022.108572',
    '10.1016/j.apenergy.2020.115336',
    '10.1016/j.ijepes.2019.105483',
    '10.1016/j.est.2025.118148'
];

const titles = [
    "Data-driven distributionally robust optimization for microgrid energy management",
    "Resilience-oriented optimal operation of networked microgrids under extreme weather events",
    "Adaptive robust energy management of microgrids considering uncertainties in renewable energy and load demand",
    "Tractable two-stage robust optimal operation of microgrids with high renewable penetration",
    "Distributionally robust scheduling of microgrids with flexible loads"
];

async function check() {
    for (const doi of dois) {
        const url = 'https://api.openalex.org/works/https://doi.org/' + doi;
        try {
            const res = await fetch(url);
            if (res.ok) {
                const data = await res.json();
                console.log(`VALID: ${doi} -> ${data.title} (${data.publication_year})`);
            } else {
                console.log(`NOT FOUND/ERROR: ${doi} (Status: ${res.status})`);
            }
        } catch (e) {
            console.log(`FETCH ERROR: ${doi} -> ${e.message}`);
        }
    }
    
    for (const title of titles) {
        const url = 'https://api.openalex.org/works?search=' + encodeURIComponent(title);
        try {
            const res = await fetch(url);
            if (res.ok) {
                const data = await res.json();
                if (data.results && data.results.length > 0) {
                    const top = data.results[0];
                    console.log(`VALID TITLE: ${title} -> Found: ${top.title} (${top.publication_year})`);
                } else {
                    console.log(`ERROR TITLE: ${title} -> Not found`);
                }
            } else {
                console.log(`ERROR TITLE: ${title} (Status: ${res.status})`);
            }
        } catch (e) {
            console.log(`FETCH ERROR: ${title} -> ${e.message}`);
        }
    }
}
check();
