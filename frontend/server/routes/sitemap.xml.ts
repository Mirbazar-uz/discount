import { defineEventHandler, setHeader } from 'h3'

const SITE_URL = 'https://mirbazar.uz'

const CATEGORIES = [
  'smartphones',
  'tv',
  'laptop',
  'appliances',
  'food',
  'grocery',
  'electronics',
  'fashion',
  'other',
]

interface Store {
  slug: string
}

interface Promotion {
  id: number
  updated_at?: string
}

interface PromotionsResponse {
  promotions: Promotion[]
  total: number
}

function escapeXml(str: string): string {
  return str
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&apos;')
}

function formatDate(date?: string): string {
  if (date) {
    return new Date(date).toISOString().split('T')[0]
  }
  return new Date().toISOString().split('T')[0]
}

function buildUrl(entry: { loc: string; lastmod: string; changefreq: string; priority: string }): string {
  return [
    '  <url>',
    `    <loc>${escapeXml(entry.loc)}</loc>`,
    `    <lastmod>${entry.lastmod}</lastmod>`,
    `    <changefreq>${entry.changefreq}</changefreq>`,
    `    <priority>${entry.priority}</priority>`,
    '  </url>',
  ].join('\n')
}

export default defineEventHandler(async (event) => {
  const config = useRuntimeConfig()
  const apiBase = config.apiBaseServer || 'http://localhost:8000'
  const today = formatDate()

  const urls: Array<{ loc: string; lastmod: string; changefreq: string; priority: string }> = []

  urls.push({
    loc: SITE_URL,
    lastmod: today,
    changefreq: 'daily',
    priority: '1.0',
  })

  const STATIC_PAGES = ['about', 'contact', 'privacy', 'terms']
  for (const page of STATIC_PAGES) {
    urls.push({
      loc: `${SITE_URL}/${page}`,
      lastmod: today,
      changefreq: 'monthly',
      priority: '0.3',
    })
  }

  for (const category of CATEGORIES) {
    urls.push({
      loc: `${SITE_URL}/category/${category}`,
      lastmod: today,
      changefreq: 'daily',
      priority: '0.8',
    })
  }

  try {
    const stores: Store[] = await $fetch(`${apiBase}/stores`)
    for (const store of stores) {
      urls.push({
        loc: `${SITE_URL}/store/${store.slug}`,
        lastmod: today,
        changefreq: 'daily',
        priority: '0.8',
      })
    }
  } catch {
    // stores endpoint unavailable — skip dynamic store URLs
  }

  try {
    const data: PromotionsResponse = await $fetch(`${apiBase}/promotions`, {
      params: { status: 'active', limit: '500' },
    })
    for (const promo of data.promotions) {
      urls.push({
        loc: `${SITE_URL}/promotion/${promo.id}`,
        lastmod: formatDate(promo.updated_at),
        changefreq: 'weekly',
        priority: '0.6',
      })
    }
  } catch {
    // promotions endpoint unavailable — skip dynamic promotion URLs
  }

  const xml = [
    '<?xml version="1.0" encoding="UTF-8"?>',
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ...urls.map(buildUrl),
    '</urlset>',
  ].join('\n')

  setHeader(event, 'Content-Type', 'application/xml; charset=utf-8')
  setHeader(event, 'Cache-Control', 'public, max-age=3600, s-maxage=3600')

  return xml
})
